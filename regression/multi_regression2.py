#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhengzhengLiu

from numpy import genfromtxt  # genfromtxt函数创建数组表格数据
import numpy as np
from sklearn import datasets, linear_model

# 读取数据，r后边内容当做完整的字符串，忽略里面的特殊字符
dataPath = r'/eee/line-regression/TransportData.csv'
transportData = genfromtxt(dataPath, delimiter=',')  # 将路径下的文本文件导入并转化成numpy数组格式
print("transportData:", transportData)

X = transportData[:, :-1]  # 取所有行和除了最后一列的所有列作为特征向量
Y = transportData[:, -1]  # 取所有行和最后一列作为回归的值
print("X:", X)
print("Y:", Y)

# 建立回归模型
regr = linear_model.LinearRegression()
regr.fit(X, Y)
print("coefficients:", regr.coef_)  # b1,...,bp（与x相结合的各个参数）
print("intercept:", regr.intercept_)  # b0（截面）

x_pred = [102, 6]
y_pred = regr.predict(x_pred)  # 预测
print("y_pred:", y_pred)