import tensorflow as tf
import numpy as np

# '''RNN参数设置，计算8位二进制加法，因此序列长度为8，每次向place_holder中喂入batch_size大小的数据，包括两个相加的二进制序列和一个结果二进制序列,hidden_size表示RNN的隐层节点维数'''
sequence_length = 8
batch_size = 100
input_size = 2
hidden_size = 8
output_size = 1

# '''推断过程，即是RNN模型的构建过程'''
def inference(x_input):
    # '''将输入转换到tensorflow中RNN需要的格式'''
    x = tf.transpose(x_input, [1, 0, 2])
    x = tf.reshape(x, [-1, input_size])
    x = tf.split(0, sequence_length, x)
    #     '''构建rnn单元和rnn网络，简单两句搞定，关键在与返回值上，输出看了下，states只有两个值，应该一个是初始状态，一个是末状态，而其他的中间状态其实涵盖在outputs里了，需要直接去取就好，不知道LSTM的输出是怎样，states会不会是8个，得去试一下'''
    rnn_cell = tf.contrib.rnn.core_rnn_cell(8)
    outputs, states = tf.nn.rnn(rnn_cell, x, dtype=tf.float16)
    # '''定义输出层权值和偏置，用variable_scope和get_variable是为了变量的不重复，否则测试和训练会构建重复的variable出来，Tensorboard里面网络的graph会变的比较乱'''
    with tf.variable_scope('hidden_to_output_layer'):
        w2out = tf.get_variable('w2out', shape=[8, 1], dtype=tf.float16, initializer=tf.truncated_normal_initializer(0.0, 1.0))
        bias2out = tf.get_variable('bias2oput', shape=[1], dtype=tf.float16, initializer=tf.constant_initializer(0.0))
    outputs = tf.reshape(outputs, [-1, hidden_size])
    result = tf.nn.sigmoid(tf.matmul(outputs, w2out)+bias2out)
    result = tf.reshape(result, [data_length, -1])
    result = tf.transpose(result, [1, 0])
    return result

def Loss(logits, y_true):
    return tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits, y_true))
    #softmax_cross_entropy_with_logits will find the largest point in logits and y_ture,then compare them.

def generateBinaryDict():
    largest_number = pow(2, 8)
    int2binary={}
    binary = np.unpackbits(
        np.array([list(range(largest_number))], dtype=np.uint8).T, axis=1)
    for i in range(largest_number):
        int2binary[i] = binary[i]
    return int2binary


input_holder = tf.placeholder(tf.int32, [None, 8, 2])
label_holder = tf.placeholder(tf.int32, [None, 8])
y_pred = inference(input_holder)
loss = tf.reduce_mean(tf.square(y_pred-label_holder))
# loss = Loss(y_pred, label_holder)
# op = tf.train.GradientDescentOptimizer(0.001).minimize(loss)
op = tf.train.AdagradOptimizer(1.0).minimize(loss)
init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    binary_dict = generateBinaryDict()
    epochs = 10000
    for e in range(epochs):
        batch_in_data = []
        batch_out_data = []
        reshape_bi_list = []
#         '''生成minibatch data，其实没必要，但是为了规范'''
        for i in range(batch_size):
            x_int1 = np.random.randint(0, 128)
            x_int2 = np.random.randint(0, 128)
            y_true_int = x_int1 + x_int2

            x_bi1 = binary_dict[x_int1]
            x_bi2 = binary_dict[x_int2]
            y_true_bi = binary_dict[y_true_int]
#             '''注意输入和输出都需要反向，因为建的RNN是从前往后传信息的，而二进制加法的进位规则是从后往前计算并进位的'''
            for j in range(8):
                reshape_bi_list.append(x_bi1[7-j])
                reshape_bi_list.append(x_bi2[7-j])
            batch_out_data.append(y_true_bi[::-1])

        batch_in_data = np.reshape(reshape_bi_list, [-1, 8, 2])
        batch_out_data = np.reshape(batch_out_data, [-1, 8])

        sess.run(op, feed_dict={input_holder: batch_in_data, label_holder: batch_out_data})
        loss_value = sess.run(loss, feed_dict={input_holder: batch_in_data, label_holder: batch_out_data})
        print(('iteration at: % d, mean loss is: %f' % (e, loss_value)))

#         '''Test part'''
        x_int1_test = np.random.randint(0, 128)
        x_int2_test = np.random.randint(0, 128)
        y_true_int_test = x_int1_test + x_int2_test

        x_bi1_test = binary_dict[x_int1_test]
        x_bi2_test = binary_dict[x_int2_test]
        y_bi_true = binary_dict[y_true_int_test]
        batch_in_test = []
        reshape_bi_list_test = []
        # batch_in_test.append(np.concatenate((x_bi1_test[::-1], x_bi2_test[::-1]), axis=0))
        for k in range(8):
            reshape_bi_list_test.append(x_bi1_test[7 - k])
            reshape_bi_list_test.append(x_bi2_test[7 - k])
        batch_in_test = np.reshape(reshape_bi_list_test, [1, 8, 2])

        test_result = sess.run(y_pred, feed_dict={input_holder: batch_in_test})
        print(('x_bi1_test: ', x_bi1_test))
        print(('x_bi2_test: ', x_bi2_test))
        print(('true_result:', y_bi_true))
        print(('predict:    ', np.int8(np.round(test_result)[0][::-1])))