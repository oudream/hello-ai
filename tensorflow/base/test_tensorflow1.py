
import numpy as np
import tensorflow as tf

arr1 = np.array([])

tensor1 = tf.Tensor()
tensor1.eval()

def my_func(arg):
  arg = tf.convert_to_tensor(arg, dtype=tf.float32)
  return tf.matmul(arg, arg) + arg

# The following calls are equivalent.
value_1 = my_func(tf.constant([[1.0, 2.0], [3.0, 4.0]]))
value_2 = my_func([[1.0, 2.0], [3.0, 4.0]])
value_3 = my_func(np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32))

init = tf.global_variables_initializer()

# Using the `close()` method.
sess = tf.Session()
sess.run([value_1])
sess.close()

tf.Constant
tf.constant()
tf.constant_initializer

print(value_1)
print(value_2)
print(value_3)
