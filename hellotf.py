import tensorflow as tf
hello = tf.constant("hellotf")
sess = tf.Session()
print(sess.run(hello))