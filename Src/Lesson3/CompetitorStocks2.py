# importing all the relevant libraries
import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime.now()

dfcomp = web.DataReader(['AAPL', 'GE', 'GOOG', 'IBM', 'MSFT'],'google', start=start, end=end)['Close']
print(dfcomp.tail)
# print(dfcomp.shape)

# finding the % change for the Closing price specified by periods
# periods accounts for the shift in periods like 1600 = 1863 - 1600 = 263 periods at the start of dataframe
retscomp = dfcomp.pct_change(periods=1)

# Showing the returns comparison
corr = retscomp.corr()
print(corr)

import matplotlib.pyplot as plt
from matplotlib import style

import matplotlib as mpl
# Showing the scatter plot for GOOG and MSFT
# plt.scatter(retscomp.GOOG, retscomp.MSFT)
# plt.xlabel('Returns GOOG')
# plt.ylabel('Returns MSFT')

# Scatter matrix with all the competition KDE -> Kernel density Estimate
# You can do scatter matrix with all the competitors data and find the kde of each m KDE will determine if your chart is more normally distributed leaning to the
# left: Returns are more likely to be negative in the long run
# centre: Returns are more likely to be 0 in the long run
# right: Returns are more likely to be positive in the long run
# pd.scatter_matrix(retscomp, diagonal='kde', figsize=(10, 10));

# showing plt.imshow to show a gridmap of x and y axis
# plt.imshow(corr, cmap='hot', interpolation='none')
# plt.colorbar()
# plt.xticks(range(len(corr)), corr.columns)
# plt.yticks(range(len(corr)), corr.columns)

# Stocks mean and Risk Calculation
plt.scatter(retscomp.mean(), retscomp.std())
plt.xlabel('Expected returns')
plt.ylabel('Risk')

for label, x, y in zip(retscomp.columns, retscomp.mean(), retscomp.std()):
    plt.annotate(
        label, 
        #label xtext specifies the location of where the text is placed on point
        xy = (x, y), xytext = (40, -30),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.1', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))






