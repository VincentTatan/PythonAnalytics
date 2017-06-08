# -*- coding: utf-8 -*-
"""
Created on Wed May 24 15:00:33 2017

@author: Alvin Toh
"""
import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime.now()
df = web.DataReader("AAPL", 'google', start, end)

# print(df.tail())
# print(df.shape)

#Plotting the moving average of dataframe

close_px= df['Close']
mavg = close_px.rolling(window=100).mean()
mavg.tail()

import matplotlib.pyplot as plt
from matplotlib import style

import matplotlib as mpl

#Adjusting the size of matplotlib
mpl.rc('figure', figsize=(8,7))
mpl.__version__

#Adjusting the size of matplotlib
style.use('ggplot')

#Plot the closing prices for apple 
close_px.plot(label='AAPL')
mavg.plot(label='mavg')
plt.legend()

#plot the closing prices for apple in percentage
# rets = close_px / close_px.shift(1) - 1 
# rets.plot(label='return')

