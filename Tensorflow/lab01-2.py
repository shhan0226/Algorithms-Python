import tensorflow as tf

# 앞쪽 레이어의 노드 빌드하기
node1 = tf.constant([1, 2], tf.float32)
node2 = tf.constant([2, 5], tf.float32)

# node3을 함수로 정의하기
@tf.function
def forward() :
    return node1 + node2

out_a = forward()
print(out_a)

###############################
# 세션과 플레이스홀더 사라짐

# sess = tf.Session() --> 없어짐

# print(sess.run()) --> tf.print()

# a = tf.placeholder(tf.float32)  --> A = tf.constant(...)

# addre_node = a + b
# -->
# @tf.function
# def adder(a, b):
#   return a + b
