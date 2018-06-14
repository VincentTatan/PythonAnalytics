import tensorflow as tf

a = tf.constant(6.5,name='constant_a')
b = tf.constant(3.4,name='constant_b')
c = tf.constant(3.0,name='constant_c')
d = tf.constant(100.2,name='constant_d')

square = tf.square(a,name="square_a")
power = tf.pow(b,c,name="pow_b_c")
sqrt = tf.sqrt(d,name="sqrt_d")

final_sum = tf.add_n([square,power,sqrt],name="final_sum")

sess =tf.Session()

print ("Square of a: ",sess.run(square))
print ("Pow of b ^ c: ",sess.run(power))
print ("sqrt of d: ",sess.run(sqrt))

print ("Sum of square, pow, and sqrt",sess.run(final_sum))

writer = tf.summary.FileWriter('./m2_example2',sess.graph)
sess.close()
writer.close()


