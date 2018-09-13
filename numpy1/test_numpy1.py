import numpy as np
from numpy.random import rand
from numpy.linalg import solve, inv

print('testNumpy1')


def testNumpy11():
    print('...testNumpy11')
    x = np.array([1, 2, 3])
    print(x)
    y = np.arange(10)
    print(y)
    a = np.arange(15).reshape(3, 5)
    print(a)
    f = np.float32(1.0)
    print(f)
    print('---testNumpy11')


testNumpy11()


def testNumpy12():
    print('...testNumpy12')
    a = np.array([1, 2, 3, 6, 7])
    b = np.linspace(1, 4, 5)  # 建立一個array, 在0與2的範圍之間讓4個點等分
    c = a - b
    print(b)
    print(c)
    print('---testNumpy12')


testNumpy12()


def testNumpy13():
    print('---testNumpy13')
    a = np.array([[1, 2, 3], [3, 4, 6.7], [5, 9.0, 5]])
    print((a.transpose()))
    print((inv(a)))
    b = np.array([3, 2, 1])
    c = solve(a, b)  # 解方程式 ax = b
    print(c)
    print('---testNumpy13')


testNumpy13()


# 例如我们要解一个这样的二元一次方程组：
# x + 2y = 3
# 4x ＋ 5y = 6
def testNumpySolve1():
    print('...testSolve1')

    def solve11():
        print('...solve11')
        A = np.mat('1,2; 4,5')  # 构造系数矩阵 A
        b = np.mat('3,6').T  # 构造转置矩阵 b （这里必须为列向量）
        r = np.linalg.solve(A, b)  # 调用 solve 函数求解
        print(r)
        print('---solve11')
    solve11()

    print('---testSolve1')

testNumpySolve1()
