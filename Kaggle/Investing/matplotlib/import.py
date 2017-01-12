import matplotlib.pyplot as plt
import numpy as np 
'''
import csv

x=[]
y=[]

with open('data.txt','r') as csvfile:
	plots = csv.reader(csvfile,delimiter=',')
	for row in plots:
		x.append(int(row[0]))
		y.append(int(row[1]))

plt.plot(x,y,label='Loaded from file')
'''

'''
x,y = np.loadtxt('data.txt',delimiter=',',unpack=True)
plt.plot(x,y,label='Loaded from file')
'''
def graph_data(stock):
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Interesting graph')
	plt.legend()
	plt.show()

graph_data("TSLA")