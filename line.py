import matplotlib.pyplot as plt
import csv
import numpy as np

x1=[1,2,3]
y1=[5,7,4]

x2=[1,2,3]
y2=[10,14,12]

x, y = [] , []

x , y = np.loadtxt('ex.csv', delimiter=',', unpack=True)

# # Loading from file using method 2:
# with open('ex.csv', 'r') as f:
#     plots = csv.reader(f, delimiter=',')
#     for row in plots:
#         x.append(int(row[0]))
#         y.append(int(row[1]))

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

ax1.plot(x1,y1, label='first line')
plt.plot(x2,y2, label='second line')
plt.plot(x, y , label='third line (loaded from file)')
plt.xlabel('Plot Number')
plt.ylabel('Important number')
plt.title('interesting graph\nCheck it out')
plt.legend()
plt.show()
