import tensorflow as tf

x = tf.placeholder("float", shape=[None, 512, 512, 3])
print(x.shape)
y_ = tf.placeholder("float", shape=[None, 5])
print(y_.shape)
exit()
keep_prob = tf.placeholder("float")