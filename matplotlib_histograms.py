import matplotlib.pyplot as plt

blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

plt.hist(x=[blood_sugar_men,blood_sugar_women],bins=[80,100,125,150], rwidth=0.95,color=['r','b'], histtype='bar',label=['men','women'], orientation='horizontal')



plt.ylabel("Sugar Level")
plt.xlabel("Number Of Patients")
plt.title("Blood Sugar Chart")

plt.legend(loc ='best', shadow=True, fontsize = 10)


plt.savefig(r'C:\Users\ritis\PycharmProjects\CSV Files\Misc\histogram.pdf', bbox_inches ='tight', pad_inches =2, transparent=True)
#saving a chart in an external folder

plt.show()