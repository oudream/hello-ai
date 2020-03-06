#!/usr/bin/env python
# coding: utf-8

# In[49]:


# common function

def printDim1(dim1):
    for c in dim1:
        print(c, end=" ")
    print()


def printDim2(dim2):
    for r in dim2:
        for c in r:
            print(c, end=" ")
        print()


# In[50]:


# data is org input data
data = [
    [100, 4, 9.3],
    [50, 3, 4.8],
    [100, 4, 8.9],
    [100, 2, 6.5],
    [50, 2, 4.2],
    [80, 2, 6.2],
    [75, 3, 7.4],
    [65, 4, 6.0],
    [90, 3, 7.6],
    [90, 2, 6.1]
]

dataRowCount = len(data)
dataColCount = len(data[0])
yIndex = dataColCount - 1

printDim2(data)

# In[51]:


# total is sum of data
total = [0 for i in range(dataColCount)]


def initTotal():
    global total
    for i in range(len(total)):
        total[i] = 1
    total = [0] * len(total)


initTotal()
printDim1(total)

# aver is average of data
aver = [0 for i in range(dataColCount)]


def initAver():
    global aver
    aver = [0] * len(aver)


initAver()
printDim1(aver)


# In[52]:


###
# calc total and average from data (input)
###
def calcTotal():
    initTotal()
    for r in data:
        for i in range(len(r)):
            total[i] += r[i]


calcTotal()
printDim1(total)


def calcAver():
    initAver()
    for i in range(len(total)):
        aver[i] = total[i] / len(data)


calcAver()
printDim1(aver)

# In[53]:


# def multiple linear regression
# def simple linear regression's b1sons=sum((xi - aver(x))(yi-aver(y)))
# def simple linear regression's b1mothers=sum(power(xi - aver(x)))

b1sons = [[0 for i in range(dataColCount - 1)] for j in range(dataRowCount)]


def calcB1sons():
    for j in range(dataColCount - 1):
        for i in range(dataRowCount):
            n1 = (data[i][j] - aver[j])
            n2 = (data[i][yIndex] - aver[yIndex])
            b1sons[i][j] = n1 * n2


calcB1sons()
printDim2(b1sons)

b1mothers = [[0 for i in range(dataColCount - 1)] for j in range(dataRowCount)]


def calcB1mothers():
    for j in range(dataColCount - 1):
        for i in range(dataRowCount):
            n1 = (data[i][j] - aver[j])
            b1mothers[i][j] = n1 * n1


calcB1mothers()
printDim2(b1mothers)

# In[48]:


###
# calc b1
###

totalB1sons = [0 for i in range(dataColCount - 1)]


def calcTotalB1sons():
    for j in range(dataColCount - 1):
        totalBlson = 0
        for i in range(dataRowCount):
            totalBlson += b1sons[i][j]
        totalB1sons[j] = totalBlson


calcTotalB1sons()
printDim1(totalB1sons)

totalB1mothers = [0 for i in range(dataColCount - 1)]


def calcTotalB1mothers():
    for j in range(dataColCount - 1):
        totalBlmother = 0
        for i in range(dataRowCount):
            totalBlmother += b1mothers[i][j]
        totalB1mothers[j] = totalBlmother


calcTotalB1mothers()
printDim1(totalB1mothers)

# In[ ]:




