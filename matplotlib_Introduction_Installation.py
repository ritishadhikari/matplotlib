import matplotlib.pyplot as plt

x =[1,2,3,4,5,6,7]
y = [50,51,52,48,47,49,46]
plt.xlabel("Day of week")
plt.ylabel("Temperature in Farenheit")
plt.title("Weather Data")
plt.plot(x,y,color = 'green',linestyle = 'dotted',linewidth = 3, alpha =0.24) #alpha is used to control the transparency
plt.show()