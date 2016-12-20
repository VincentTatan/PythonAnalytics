from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import seaborn as sns

m = Basemap(projection='mill',
            llcrnrlat = 25,
            llcrnrlon = -130,
            urcrnrlat = 50,
            urcrnrlon = -60,
            resolution='l')
# m = Basemap('mill')

m.drawcoastlines()
m.drawcountries(linewidth=2)
m.drawstates(color='b')
##m.drawcounties(color='darkred')
#m.fillcontinents()
# m.etopo()
# m.bluemarble()
xs=[]
ys=[]

NYClat,NYClon = 40.7127,-74.0059
xpt,ypt = m(NYClon,NYClat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt,ypt,'c*',markersize=15,label='Departure')

LAlat, LAlon = 34.05, -118.25
xpt, ypt = m(LAlon, LAlat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt, ypt, 'g^', markersize=15,label='Destination')

m.plot(xs,ys,linewidth=3,color='r',label='Flight 98')
m.drawgreatcircle(NYClon,NYClat,LAlon,LAlat,linewidth=3,label='Arc')

plt.legend(loc=4)
plt.title('Basemap Tutorial')
plt.show()