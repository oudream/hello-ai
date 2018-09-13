# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:01:31 2017
@author: sl169
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import tempfile

from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf

SUMMARY_DIR = "../../logs/supervisor.log"
BATCH_SIZE = 100
TRAIN_STEPS = 3000


# 生成变量监控信息并定义生成监控信息日志的操作，var是需要记录的张量，name为可视化结果
# 中显示的图标名称
def variable_summaries(var, name):
    with tf.name_scope('summaries'):
        # 记录张量中元素的取值分布
        tf.summary.histogram(name, var)

        # 计算变量平均值，mean为命名空间
        mean = tf.reduce_mean(var)
        tf.summary.scalar('mean/' + name, mean)

        # 计算变量的标准差
        stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
        tf.summary.scalar('stddev/' + name, stddev)


# 生成一层全链接的神经网络
def nn_layer(input_tensor, input_dim, output_dim, layer_name, act=tf.nn.relu):
    with tf.name_scope(layer_name):
        with tf.name_scope('weights'):
            # 声明神经网络边上的权重，并调用生成权重监控日志的函数
            weights = tf.Variable(tf.truncated_normal([input_dim, output_dim], stddev=0.1))
            variable_summaries(weights, layer_name + '/weights')
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.constant(0.0, shape=[output_dim]))
            variable_summaries(biases, layer_name + '/biases')
        with tf.name_scope('Wx_plus_b'):
            preactivate = tf.matmul(input_tensor, weights) + biases
            # 记录神经网络输出节点在经过激活函数之前的分布
            tf.summary.histogram(layer_name + '/pre_activations', preactivate)
        activations = act(preactivate, name='activation')

        # 记录神经网络节点输出在经过激活函数之后的分布。
        # 对于layer1因为使用了ReLU激活函数，所以所有小于0的值都设为0了，于是
        # 在激活后的layer1/activations上所有值都是大于0的，而对于layer2，因为
        # 没有使用激活函数，所以layer2/activations和layer2/pre_activations一样
        tf.summary.histogram(layer_name + '/activations', activations)
        return activations


def main():
    mnist = input_data.read_data_sets("../../MNIST/MNIST_data/", one_hot=True)

    with tf.name_scope('input'):
        x = tf.placeholder(tf.float32, [None, 784], name='x-input')
        y_ = tf.placeholder(tf.float32, [None, 10], name='y-input')

    # 将输入向量还原成图片的像素矩阵，并将图片信息写入日志
    with tf.name_scope('input_reshape'):
        image_shaped_input = tf.reshape(x, [-1, 28, 28, 1])
        tf.summary.image('input', image_shaped_input, 10)

    hidden1 = nn_layer(x, 784, 500, 'layer1')
    y = nn_layer(hidden1, 500, 10, 'layer2', act=tf.identity)

    # 计算交叉熵并生成交叉熵的日志
    with tf.name_scope('cross_entropy'):
        cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y, labels=y_))
        tf.summary.scalar('cross_entropy', cross_entropy)

    with tf.name_scope('train'):
        train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

    # 计算模型在当前给定数据上的正确率，并定义生成正确率监控日志的操作
    with tf.name_scope('accuracy'):
        with tf.name_scope('correct_prediction'):
            correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        with tf.name_scope('accuracy'):
            accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        tf.summary.scalar('accuracy', accuracy)

    # 上面那些定义监控日志的操作不会立刻执行，需要通过sess.run来明确调用这些函数，
    # 写日志操作比较多的时候，一一调用比较麻烦，所以TensorFlow提供了summary.merge_all
    # 函数来整理所有的日志生成操作
    merged = tf.summary.merge_all()

    with tf.Session() as sess:
        summary_writer = tf.summary.FileWriter(SUMMARY_DIR, sess.graph)
        tf.global_variables_initializer().run()

        for i in range(TRAIN_STEPS - 2800):
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            # 运行训练步骤以及所有的日志生成操作，得到这次运行的日志。
            summary, _ = sess.run([merged, train_step], feed_dict={x: xs, y_: ys})
            # 将得到的所有日志写入日志文件，这样TensorBoard程序就可以拿到这次运行所对应的
            # 运行信息。
            summary_writer.add_summary(summary, i)

    summary_writer.close()


if __name__ == '__main__':
    main()


    tf.constant_initializer