
import tensorflow as tf
import numpy as np

# 这里是numpy的用法
matrix_01 = np.zeros((3, 4))
print(matrix_01)
# 这里是numpy的reshape
matrix_03 = np.reshape(matrix_01, (6, 2))
print(matrix_03)

# tensorflow的用法
matrix_02 = tf.zeros((3, 4))
print(matrix_02)
matrix_04 = tf.reshape(matrix_02, (6, 2), name="add")
print(matrix_04)

a = tf.add(3, 5)
print(a)
with tf.Session() as session:
    print(session.run(a))
    print(a)

x = 2
y = 3
operation01 = tf.add(x, y)
operation02 = tf.multiply(x, y)
operation03 = tf.pow(operation01, operation02)
with tf.Session() as session01:
    operation04 = session01.run(operation03)
    print(operation04)


num01 = tf.constant(2)
num02 = tf.constant(3)

operation05 = tf.add(num01, num02)

with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs/const_add', session.graph)
    print(session.run(operation05))

writer.close()


# multiply是点乘
a = tf.constant([1,4], name='a')
b = tf.constant([[0,1],[2, 3]], name='b')
x = tf.multiply(a, b, name='dot_multiply')
with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs/const_dot_mul', session.graph)
    print(session.run(x))
writer.close()

# matmul是矩阵乘法
a = tf.constant([[1,4], [2, 4]], name='a')
b = tf.constant([[0,1],[2, 3]], name='b')
x = tf.matmul(a, b, name='matrix_multiply')
with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs/const_matrix_mul', session.graph)
    print(session.run(x))
writer.close()

# 重新再来一遍
x = 2
y = 3
add_op = tf.add(x, y)
mul_op = tf.multiply(x, y)
useless = tf.multiply(x, add_op)
pow_op = tf.pow(add_op, mul_op)
with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs/const_show_mul', session.graph)
    m, n = session.run([pow_op, useless])













































