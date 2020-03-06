import numpy as np
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Flatten, Dense, Dropout
from keras.utils import np_utils
from keras.datasets import mnist

# 加载MNIST数据集，其中包含60,000个训练样本、10,000个测试样本
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 调整加载数据的形态
X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

model = Sequential()

# 添加第一个卷积层，其中，超参数32,3,3分别表示“过滤器的个数、过滤器的宽、过滤器的高”
# input_shape = (1, 28, 28)表示“输入图片的深度为1，宽度为28，高度为28”
model.add(Convolution2D(32, 3, 3, input_shape=(1, 28, 28)))

# 添加激活层（ReLU）
model.add(Activation('relu'))

# 添加第二个卷积层
# 除第1层卷积外，其余各层卷积均不再需要输入input_shape，算法会自动识别其形态
model.add(Convolution2D(32, 3, 3))

# 添加激活层（ReLU）
model.add(Activation('relu'))

# 添加池化层
model.add(MaxPooling2D(pool_size=(2, 2)))

# 添加展开层，因为，在“全连接层”之前，需要先将图片的像素值展开
model.add(Flatten())

# 添加第1个全连接层
# “128”表示神经元的个数，可以设置为任意数值
model.add(Dense(128, activation='relu'))

# 添加dropout层，防止过拟合
model.add(Dropout(0.5))

# 添加第2个全连接层
# “10”表示神经元的个数，但是由于本层为CNNs架构的最后一层（即“输出层”），
# 所以，此处的数值只能为“10”，对应“0-9”个数字分类
# “softmax”是非线性函数，输出的结果为“最初输入的图片，属于每种类别的概率”
model.add(Dense(10, activation='softmax'))

# 编译模型
# 告诉模型，我们的目标是要使得“误差损失：categorical_crossentropy”尽可能小
# 为了实现这一“目标”，所使用的优化方法是：adam
# 使用“准确率：accuracy”来评估模型的预测效果
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# 训练模型
# batch_size=32 表示一批处理32个样本
# nb_epoch=10 表示10个周期，每个周期都把全部60,000个样本遍历一遍
# validation_split=0.3 表示从训练样本中拿出30%作为交叉验证集
model.fit(X_train, Y_train,
          batch_size=32, nb_epoch=10, validation_split=0.3)

# 评估模型
score = model.evaluate(X_test, Y_test)
print(score)