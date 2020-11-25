import tensorflow as tf
tf.__version__

print(tf)

# Create a constant op
# This op is added as a node to the default graph
hello = tf.constant("Hello, TensorFlow!")

# start a TF session
# sess = tf.Session()

# run the op and get result
print(hello)