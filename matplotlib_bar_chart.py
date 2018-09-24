import matplotlib.pyplot as plt
import numpy as np

company=['GOOGL','AMZN','MSFT','FB']
revenue=[90,136,89,27]
profit =[40,2,34,12]

ypos =np.arange(len(company)) #make the variable as xpos for normal bar

plt.yticks(ypos,company) #replace yticks by xticks for normal bar

plt.barh(ypos-0.2,revenue, label ='Revenue', height =0.4)  #replace height by width for normal bar
plt.barh(ypos+0.2,profit, label ='Profit', height =0.4)
plt.ylabel("Revenues in US Billion Dollars")
plt.title("US Tech Talks")

plt.legend()
plt.grid(color ='gold', linestyle =':')

plt.savefig(r'C:\Users\ritis\PycharmProjects\CSV Files\Misc\barchart.pdf', bbox_inches ='tight', pad_inches =2, transparent=True)
#saving a chart in an external folder

plt.show()