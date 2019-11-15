import numpy as np
import matplotlib.pyplot as plt

x = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]

y = [63,10,18,27,31,36,52,45,48,60,43,52,36,50,30,23,13,12,9,20]

fig, ax = plt.subplots()

ax.stackplot(x,y)
ax.set_xlim(xmin=x[0], xmax=x[-1])
fig.set_facecolor('floralwhite')
ax.set_ylabel('Problems Available')
ax.set_xlabel('Difficulty Rating')
ax.set_facecolor('seashell')
fig.set_figwidth(20)
plt.show()