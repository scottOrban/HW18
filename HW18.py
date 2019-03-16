# Task 1
#import pandas as pd
#df=pd.read_excel('data_tasks.xlsx',sheet_name='task1')
#
#temp = df.values[:,1]
#time = df.values[:,0]
#stdDev = df.values[:,2]
#
#import matplotlib.pyplot as plt
#line, caps,bars=plt.errorbar(
#        time, 
#        temp, 
#        yerr = stdDev, 
#        fmt = 'bs--', 
#        linewidth=3,
#        elinewidth=0.5,
#        ecolor='k',
#        capsize=5,
#        capthick=1
#        )
#
#plt.legend(["Error Bars"],numpoints=1,loc=("upper left"))
#plt.savefig('task1.png', dpi=600)
#plt.show()


# Task 2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#df2=pd.read_excel('data_tasks.xlsx',sheet_name='task2')
#
#time = df2.values[1:7,0]

## Figure 1
#LV_Temp = df2.values[1:7,1]
#LV_StdDev = df2.values[1:7,2]
#
#line,caps,bars=plt.errorbar(
#        time, 
#        LV_Temp, 
#        yerr = LV_StdDev, 
#        fmt = 'bs--', 
#        linewidth=3,
#        elinewidth=0.5,
#        ecolor='k',
#        capsize=5,
#        capthick=1
#        )
#plt.title("Las Vegas", fontsize=24)
#plt.xlabel("Time (Hr)", fontsize=14)
#plt.ylabel("Temperature (C)", fontsize=14)
#plt.legend(["Error Bars"],numpoints=1,loc=("upper left"))
#plt.savefig('task2-1.png', dpi=600)
#plt.show()


## Figure 2
#DU_Temp = df2.values[1:7,3]
#DU_StdDev = df2.values[1:7,4]
#
#line,caps,bars=plt.errorbar(
#        time, 
#        DU_Temp, 
#        yerr = DU_StdDev, 
#        fmt = 'rs--', 
#        linewidth=3,
#        elinewidth=0.5,
#        ecolor='k',
#        capsize=5,
#        capthick=1
#        )
#plt.title("Durango", fontsize=24)
#plt.xlabel("Time (Hr)", fontsize=14)
#plt.ylabel("Temperature (C)", fontsize=14)
#plt.legend(["Error Bars"],numpoints=1,loc=("upper left"))
#plt.savefig('task2-2.png', dpi=600)
#plt.show()


## Figure 3
#DV_Temp = df2.values[1:7,5]
#DV_StdDev = df2.values[1:7,6]
#
#line,caps,bars=plt.errorbar(
#        time, 
#        DV_Temp, 
#        yerr = DV_StdDev, 
#        fmt = 'gs--', 
#        linewidth=3,
#        elinewidth=0.5,
#        ecolor='k',
#        capsize=5,
#        capthick=1
#        )
#plt.title("Denver", fontsize=24)
#plt.xlabel("Time (Hr)", fontsize=14)
#plt.ylabel("Temperature (C)", fontsize=14)
#plt.legend(["Error Bars"],numpoints=1,loc=("upper left"))
#plt.savefig('task2-3.png', dpi=600)
#plt.show()


## Figure 4
barWidth = 0.25

highBar = [50,28,20]
lowBar = [38,20,7]
avBar = [43,23.7,13.6]

highErrBar = [3,3,3]
lowErrBar = [2,3,4]
avErrBar = [3.3,3.3,3.3]

r1=np.arange(len(highBar))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.bar(r1, highBar, color ='#7f6d5f', width = barWidth, edgecolor = 'white', label = 'High Temps', yerr = highErrBar, capsize = 5)
plt.bar(r2, lowBar, color ='#557f2d', width = barWidth, edgecolor = 'white', label = 'Low Temps', yerr = lowErrBar, capsize = 5)
plt.bar(r3, avBar, color ='#2d7f5e', width = barWidth, edgecolor = 'white', label = 'Average Temps', yerr = avErrBar, capsize = 5)

plt.xlabel('City', fontweight='bold')
plt.ylabel('Temperature (C)', fontweight='bold')
plt.xticks([r+barWidth for r in range(len(highBar))], ['Las Vegas', 'Durango', 'Denver'])
plt.legend()
plt.savefig('task2-4.png', dpi=600)






