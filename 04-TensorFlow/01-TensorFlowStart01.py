import tensorflow as tf


# 获取某一tensor的秩，也就是维度
node9 = tf.Tensor([[3.0, 2.0], [1, 2], [2, 3]])
r = tf.rank(node9)
print(r)