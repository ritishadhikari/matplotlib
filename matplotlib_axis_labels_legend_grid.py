import matplotlib.pyplot as plt

days=[1,2,3,4,5,6,7]
max_t=[50,51,52,48,47,49,46]
min_t=[43,42,40,44,33,35,37]
avg_t=[45,48,48,46,40,42,41]

plt.plot(days,max_t,label ='Maximum Temperature')
plt.plot(days,min_t, label = 'Minimum Temperature')
plt.plot(days,avg_t, label ='Average Temperature')
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Weather")

plt.legend(loc ='best', shadow=True, fontsize = 10)
plt.grid(color ='grey', linestyle =':')
plt.show()