 # want to know more about how the code works, see that tutorial. Otherwise:

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("twitter-out.txt","rb").read()
    lines = pullData.split('\n')

    xar=[]
    yar=[]

    x=0
    y=0

    for l in lines[-200:]:

        # print("hello",l,xar,yar)
        x+=1
        if "pos" in l:
            y+=1
        if "neg" in l:
            y-=1
        xar.append(x)
        yar.append(y)

        
    ax1.clear()
    ax1.legend()
    ax1.plot(xar,yar,label='Positive/Negative')
   

ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()
