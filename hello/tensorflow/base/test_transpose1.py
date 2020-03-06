import numpy as np
import tensorflow as tf

#x = tf.constant([[1, 2 ,3],[4, 5, 6]])
x = [[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[21,22,23,24],[25,26,27,28],[29,30,31,32]]]
#a=tf.constant(x)
a=tf.transpose(x, [0, 1, 2])
b=tf.transpose(x, [0, 2, 1])
c=tf.transpose(x, [1, 0, 2])
d=tf.transpose(x, [1, 2, 0])
e=tf.transpose(x, [2, 1, 0])
f=tf.transpose(x, [2, 0, 1])

# 'perm' is more useful for n-dimensional tensors, for n > 2
# 'x' is   [[[1  2  3]
#            [4  5  6]]
#           [[7  8  9]
#            [10 11 12]]]
# Take the transpose of the matrices in dimension-0
#tf.transpose(b, perm=[0, 2, 1])
with tf.Session() as sess:
    print ('---------------x - shape: ', end='')
    print (np.array(x).shape, end='')
    print (':')
    print (x)
    print ('---------------a ', end='')
    print (type(a), end=''), print (' - shape: ', end='')
    print (a.get_shape())
    print (sess.run(a))
    print ('---------------b ', end='')
    print (type(b), end=''), print (' - shape: ', end='')
    print (b.get_shape())
    print (sess.run(b))
    print ('---------------c ', end='')
    print (type(c), end=''), print (' - shape: ', end='')
    print (c.get_shape())
    print (sess.run(c))
    print ('---------------d ', end='')
    print (type(d), end=''), print (' - shape: ', end='')
    print (d.get_shape())
    print (sess.run(d))
    print ('---------------e ', end='')
    print (type(e), end=''), print (' - shape: ', end='')
    print (e.get_shape())
    print (sess.run(e))
    print ('---------------f ', end='')
    print (type(f), end=''), print (' - shape: ', end='')
    print (f.get_shape())
    print (sess.run(f))
    print ('---------------end.')