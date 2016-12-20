import matplotlib.pyplot as plt


x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

x2 = [1,2,3,4,5,6,7,8]
y2 = [1,1,1,1,1,1,1,1]
# ids= [x for x in range(len(population_ages))]
plt.scatter(x,y,label='skitscat',color='k',s=25,marker='*')
plt.scatter(x2,y2,label='skitscat',color='r',s=25,marker='o')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph\nCheck it out')
plt.legend()
plt.show()