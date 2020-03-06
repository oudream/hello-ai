def testFunction(fn):
    type(fn)

def testPythonList1():
    a = list(range(10))
    print(a[5:8])

print('')

def testArray1():
    import numpy as np
    a = np.array(range(10))
    print(a[5:8])

    str

def testArray2():
    import numpy as np
    a = np.array(range(90)).reshape(3, 10, 3)
    print(a[:2, :2])
    print(a.ndim)
    print(a.size)


def testArra3():
    '''
    numpy库为python提供了很多方便的数学计算方法，尤其是提供了数组，极大方便了使用python进行矩阵运算，
    使其在机器学习和深度学习中得到有效利用，本文详细介绍一下高维矩阵的切割问题。
    平时我们使用最多的就是一，二维和三维矩阵，以前我容易将其跟立体几何联系起来。后来发现这样是非常错误的，
    因为再高一点的维度就不能想象了。所以，按照矩阵的形式，从外向内，逐层分解才能掌握好矩阵。
    :return:
    '''
    import numpy as np

    a=np.arange(10)
    print(a)
    print(a[0:9])  # 包头不包尾
    print(a[3:6])
    print(a[:5])  # :前面不写就是从下标为0开始
    print(a[5:])  # :后面不写就是一直到最后一个元素
    print(a[:])   # :前后都不写就是从头到尾

    print('---------------')
    '''
    多维矩阵按括号的层级，从外向内，一次是第1，2，3，...维
    
    b[]内用逗号将各维分开，分别代表第1,2,3...维元素
    
    每个维度上都有自己的下标，也可以用':'取部分
    '''
    b= np.mat(np.arange(20).reshape(4,5))
    print(b)
    print(b[1:3,2:5])   # 先取第一维中下标为1,2的2部分，再取第二维中下标为2,3,4的3部分
    print(b[:2,2:])     # 同理，前面不写从头开始，后面不写一直到末尾
    print(b[:2,3])      # 当然，也可以在某维度上只取一行

    print('-----------------')
    c= np.arange(60).reshape(3,4,5)
    print(c)
    print(c[:2,2:4,1:4])  # 从外向内一层一层的割，切割不改变矩阵维度

    print('-------------------')
    d= np.arange(240).reshape(3,4,5,4)
    print(d)
    print(d[:2,1:3,2:5,1:3])