# import tensorflow as tf
#
# a = tf.add(2, 3)
# b = tf.multiply(a, 3)
#
# with tf.Session() as session:
#     replace_dict = {a:15}
#     session.run(b, feed_dict=replace_dict)
#     print(session.run(b, feed_dict=replace_dict))
#
# y = tf.constant(0)
# c = tf.multiply(y, 5)
# with tf.Session() as session:
#     replace_dict = {y: 5}
#     print(session.run(c, feed_dict=replace_dict))

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (8, 4)

n_observations = 100
xs = np.linspace(-3, 3, n_observations)
ys = np.sin(xs) + np.random.uniform(-0.5, 0.5, n_observations)
plt.scatter(xs, ys)

# plt.show()

# 1，准备数据
X = tf.placeholder(tf.float32, name='X')
Y = tf.placeholder(tf.float32, name='Y')

# 2, 权重和偏差
Weight = tf.Variable(tf.random_normal([1]), name='weight')
bias = tf.Variable(tf.random_normal([1]), name='bias')

# 3，计算误差等
Y_pred = tf.add(tf.multiply(X, Weight), bias)
loss = tf.square(Y-Y_pred, name='loss')

# 4, 定义优化器
learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

# 5，制定迭代次数， 并在session中执行graph
n_sample = xs.shape[0]
init = tf.global_variables_initializer()

with tf.Session() as session:
    # 初始化所有变量
    session.run(init)
    writer = tf.summary.FileWriter('./graphs/linear_reg', session.graph)

    # 训练模型
    for i in range(50):
        total_loss = 0
        for x, y in zip(xs, ys):
            # 为了训练模型，需要传值进去
            _, l = session.run([optimizer, loss], feed_dict={X: x, Y: y})
            total_loss += l

        # 每隔五个打印一下损失值
        if i % 5 == 0:
            print('Eporch {0}: {1}'.format(i, total_loss/n_sample))

    # 关闭writer
    writer.close()

    resultW, resultBias = session.run([Weight, bias])

    print(resultW)
    print(resultBias)

    plt.plot(xs, ys, 'bo', label="Real_Data")
    plt.plot(xs, xs * resultW + resultBias, "r", label="Predicted_Date")
    plt.legend()
    plt.show()
































