import matplotlib.pyplot as plt
import random

x = [random.random() * 10 for _ in range(10)]
y = [random.random() * 10 for _ in range(10)]
plt.scatter(x, y, label='skitskat', color='k', marker='*', s=100)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph\nCheck it out')
plt.legend()
plt.show()
