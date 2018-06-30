import matplotlib.pyplot as plt
import random

days = [x for x in range(5)]

sleeping = [int(random.gauss(8, 3)) for x in range(5)]
eating   = [int(random.gauss(3, 3)) for x in range(5)]
working  = [int(random.gauss(7, 2)) for x in range(5)]
playing  = [int(random.gauss(8, 5)) for x in range(5)]

# it is a pie chart in vertical lines

plt.stackplot(days, sleeping, eating, working, playing)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph\nCheck it out')
plt.legend()
plt.show()
