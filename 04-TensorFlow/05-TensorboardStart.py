import tensorflow as tf



with tf.name_scope('output_act'):
    hidden = tf.nn.relu6(tf.matmul(tf.reshape, output_weights[0]) + output_biases)
    tf.histogram_summary('output_act', hidden)
