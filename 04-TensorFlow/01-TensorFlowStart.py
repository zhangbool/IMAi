import tensorflow as tf


# -------------------固定值计算----------------------------
node1 = tf.constant([[3.0, 2.0],[1, 2], [2,3]], dtype=tf.float32)
node2 = tf.constant([2, 3])  # 隐式地表示同样是tf.float32

print(node1,"\n", node2)

session = tf.Session()

print(session.run(node1))


node3 = tf.constant(3)
node4 = tf.constant(4)
print(node3)
print(node4)
print(session.run([node3, node4]))

node5 = tf.add(node3, node4)
print(session.run(node5))

node6 = tf.constant([2, 3])
node7 = tf.constant([2, 5])
node8 = tf.add(node6, node7)
print(session.run(node8))


# ----------------变量计算-------------------

W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b
#
init = tf.global_variables_initializer()
session.run(init)
print(session.run(linear_model, {x: [1, 2, 3, 4, 5]}))


y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
print(session.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))


# fixW = tf.assign(W, [-1.])
# fixb = tf.assign(b, [1.])
# session.run([fixW, fixb])
# print(session.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))


optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
for i in range(100):
    session.run(train, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]})
print(session.run([W, b]))


for i in range(1000):
    session.run(train, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]})
print(session.run([W, b]))


for i in range(10000):
    session.run(train, {x: [1, 2, 3, 4, 5], y: [0, -1, -2, -3, -4]})
print(session.run([W, b]))

