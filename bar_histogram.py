import matplotlib.pyplot as plt
import random

population_ages = [random.gauss(35, 10) for i in range(50)]

ids = [x for x in range(len(population_ages))]

bins = [0, 10, 20 ,30 ,40 ,50 ,60 ,70 , 80 , 90 , 100 , 120 , 130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph\nCheck it out')
plt.legend()
plt.show()
