import matplotlib.pyplot as plt

values = [1400, 600, 300, 410, 250]
labels = ['Home Rent', 'Food', 'Phone/Internet Bill','Car','Other Utilities']

plt.pie(x=values,labels=labels,colors=['r','b','y','g','gold','purple'],radius=6, autopct='%0.2f%%', shadow=True, explode=[0,0.7,0,0,0], startangle=60)
#autopct for displaying the percentage #explode for highligting a specific parameter
plt.axis('equal')

plt.savefig(r'C:\Users\ritis\PycharmProjects\CSV Files\Misc\piechart.pdf', bbox_inches ='tight', pad_inches =2, transparent=True)
#saving a chart in an external folder

plt.show()