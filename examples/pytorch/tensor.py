
# https://pytorch.org/docs/stable/tensors.html

import torch
import numpy as np
from torch.autograd import Variable


torch.tensor([[1., -1.], [1., -1.]])
    # tensor([[ 1.0000, -1.0000],
    #         [ 1.0000, -1.0000]])
torch.tensor(np.array([[1, 2, 3], [4, 5, 6]]))
    # tensor([[ 1,  2,  3],
    #         [ 4,  5,  6]])



### create
# 定义一个3行2列的全为0的矩阵
b = torch.zeros((3, 2))

# 定义一个3行2列的随机值矩阵
c = torch.randn((3, 2))

# 定义一个3行2列全为1的矩阵
d = torch.ones([2, 4], dtype=torch.float64, device=cuda0)
d = torch.ones((3, 2))

print(b)
print(c)
print(d)



### get set
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(x[1][2])
    # tensor(6)
x[0][1] = 8
print(x)
    # tensor([[ 1,  8,  3],
    #         [ 4,  5,  6]])



### single value:
x = torch.tensor([[1]])
tensor([[ 1]])
x.item()
    # 1
x = torch.tensor(2.5)
tensor(2.5000)
x.item()
    # 2.5



### grad
x = torch.tensor([[1., -1.], [1., 1.]], requires_grad=True)
out = x.pow(2).sum()
out.backward()
x.grad
    # tensor([[ 2.0000, -2.0000],
    #         [ 2.0000,  2.0000]])



### numpy
# 定义一个3行2列的全为0的矩阵
b = torch.randn((3, 2))

# tensor转化为numpy
numpy_b = b.numpy()
print(numpy_b)

# numpy转化为tensor
numpy_e = np.array([[1, 2], [3, 4], [5, 6]])
torch_e = torch.from_numpy(numpy_e)

print(numpy_e)
print(torch_e)


### Pytorch里面的Variable类型数据功能更加强大，相当于是在Tensor外层套了一个壳子，
# 这个壳子赋予了前向传播，反向传播，自动求导等功能，在计算图的构建中起的很重要的作用。
# 定义三个Variable变量
x = Variable(torch.Tensor([1, 2, 3]), requires_grad=True)
w = Variable(torch.Tensor([2, 3, 4]), requires_grad=True)
b = Variable(torch.Tensor([3, 4, 5]), requires_grad=True)

# 构建计算图，公式为：y = w * x^2 + b
y = w * x * x + b

# 自动求导，计算梯度
y.backward(torch.Tensor([1, 1, 1]))

print(x.grad)
print(w.grad)
print(b.grad)



### convert
tensor = torch.randn(3, 5)
print(tensor)

# torch.long() 将tensor投射为long类型
long_tensor = tensor.long()
print(long_tensor)

# torch.half()将tensor投射为半精度浮点类型
half_tensor = tensor.half()
print(half_tensor)

# torch.int()将该tensor投射为int类型
int_tensor = tensor.int()
print(int_tensor)

# torch.double()将该tensor投射为double类型
double_tensor = tensor.double()
print(double_tensor)

# torch.float()将该tensor投射为float类型
float_tensor = tensor.float()
print(float_tensor)

# torch.char()将该tensor投射为char类型
char_tensor = tensor.char()
print(char_tensor)

# torch.byte()将该tensor投射为byte类型
byte_tensor = tensor.byte()
print(byte_tensor)

# torch.short()将该tensor投射为short类型
short_tensor = tensor.short()
print(short_tensor)
