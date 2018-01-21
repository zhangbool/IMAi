from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf


mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

session = tf.InteractiveSession()

x = tf.placeholder("float", shape=[None, 784])
y_ = tf.placeholder("float", shape=[None, 10])


W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))


session.run(tf.initialize_all_variables())

y = tf.nn.softmax(tf.matmul(x,W) + b)

cross_entropy = -tf.reduce_sum(y_*tf.log(y))

cross_entropy = -tf.reduce_sum(y_*tf.log(y))