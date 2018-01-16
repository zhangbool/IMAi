import tensorflow as tf
import numpy as np


x_data = np.random.rand(100)
# print(x_data)

y_data = x_data*0.1 + 0.3
# print(y_data)


weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = weights*x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()

session = tf.Session()
session.run(init)

for i in range(201):
    session.run(train)
    if i%20 == 0:
        print(i, session.run(weights), session.run(biases))


