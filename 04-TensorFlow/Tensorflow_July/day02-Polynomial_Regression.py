import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (7, 4)

n_observations = 100
xs = np.linspace(-3, 3, n_observations)
ys = np.sin(xs) + np.random.uniform(-0.5, 0.5, n_observations)

# plt.scatter(xs, ys)
# plt.show()

X = tf.placeholder(tf.float32,  name="X")
Y = tf.placeholder(tf.float32,  name="Y")

W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

Y_pred = tf.add(tf.multiply(X, W), b)

W_2 = tf.Variable(tf.random_normal([1]), name="weight_2")
Y_pred = tf.add(tf.multiply(tf.pow(X, 2), W_2), Y_pred)
W_3 = tf.Variable(tf.random_normal([1]), name="weight_3")
Y_pred = tf.add(tf.multiply(tf.pow(X, 3), W_3), Y_pred)


sample_num = xs.shape[0]
loss = tf.reduce_sum(tf.pow(Y_pred-Y, 2))/sample_num

learning_rate = 0.01
optimizer =   tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

n_samples = xs.shape[0]

with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('./graphs/polynomial_regression', session.graph)

    for i in range(1000): 
        total_loss = 0
        for x, y in zip(xs, ys):
            _, l = session.run([optimizer, loss], feed_dict={X:x, Y:y})
            total_loss += l
        if i%20 == 0:
            print("Epoch {0}:{1}".format(i, total_loss/n_samples))

    writer.close()
    W, W_2, W_3, b = session.run([W, W_2, W_3, b])
    print("{0}, {1}, {2}, {3}".format(W, W_2, W_3, b))
    

plt.plot(xs, ys, "bo", label="Real_Data")
plt.plot(xs, xs*W + np.power(xs, 2)*W_2 + np.power(xs, 3)*W_3 + b, "r", label="Predicted_Data")
plt.legend()
plt.show()











