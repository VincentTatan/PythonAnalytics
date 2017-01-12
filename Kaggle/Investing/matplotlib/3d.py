from mpl_toolkits.mplot3d import axes3d
from matplotlib import style
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')

x = [1,2,3,4,5,6,7,8,9,10]
y = [5,6,7,8,2,5,6,3,7,2]
z = [1,2,6,3,2,7,3,3,7,2]


x2 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
y2 = [-5,-6,-7,-8,-2,-5,-6,-3,-7,-2]
z2 = [1,2,6,3,2,7,3,3,7,2]

# Making a line
# ax1.plot_wireframe(x,y,z)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

# Making scatterplots
# ax1.scatter (x,y,z,c='b',marker='*',s=100)
# ax1.scatter(x2,y2,z2,c='r',marker='o',s=100)

x3 = [1,2,3,4,5,6,7,8,9,10]
y3 = [5,6,7,8,2,5,6,3,7,2]
z3 = np.zeros(10)


dx = np.ones(10)
dy = np.ones(10)
dz = [1,2,6,3,2,7,3,3,7,2]

ax1.bar3d(x3,y3,z3,dx,dy,dz)
plt.show()