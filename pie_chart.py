import matplotlib.pyplot as plt
import random

days = [x for x in range(5)]

sleeping = [int(random.gauss(8, 1)) for x in range(5)]
eating   = [int(random.gauss(3, 3)) for x in range(5)]
working  = [int(random.gauss(7, 2)) for x in range(5)]
playing  = [int(random.gauss(8, 5)) for x in range(5)]

slices = [sleeping[0], eating[0], working[0], playing[0]]
activities = ['sleeping', 'eating', 'working', 'playing']
plt.pie(slices,
 labels=activities,
 shadow=True,
 explode=(0,0.1,0,0),
 autopct='%1.1f%%'
)

plt.title('Interesting graph\nCheck it out')
plt.legend()
plt.show()
