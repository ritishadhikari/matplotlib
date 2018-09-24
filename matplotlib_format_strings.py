import matplotlib.pyplot as plt

x =[1,2,3,4,5,6,7]
y = [50,51,52,48,47,49,46]

plt.plot(x,y,'rD--', markersize='5') #Here Color ='r', marker ='D', linestyle ='--', markersize = normal
plt.ylabel("Temperature in Farenheit")
plt.xlabel("Day of week")
plt.title("Weather Data")
plt.show()