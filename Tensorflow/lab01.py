# import tensorflow as tf
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

##########################################################
# v1
#

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

#1####
# 노드를 만들어 준다.
# 즉, 그래프를 빌드한다.
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly
node3 = tf.add(node1, node2)

#####
# 결과값이 그냥 텐서야 라고 나온다.
print("node1:", node1, "node2:", node2)
print("node3: ", node3)

#2####
# 실행을 위해서는 run을 사용한다.
# 즉, 그래프를 실행한다.
sess = tf.Session()
print("sess.run(node1, node2): ", sess.run([node1, node2]))
print("sess.run(node3): ", sess.run(node3))



##########################################################
# v2
#
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly
node3 = tf.add(node1, node2)

#1###
# 그래프 실행에서 값을 주고 싶다하면,
# 노드를 placeholder로 만들어준다.
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b  # + provides a shortcut for tf.add(a, b)

#2####
# 값을 넘겨줄때, feed_dict를 이용해 placeholder에 넘겨준다.
print(sess.run(adder_node, feed_dict={a: 3, b: 4.5}))
print(sess.run(adder_node, feed_dict={a: [1,3], b: [2, 4]}))


add_and_triple = adder_node * 3.
print(sess.run(add_and_triple, feed_dict={a: 3, b:4.5}))