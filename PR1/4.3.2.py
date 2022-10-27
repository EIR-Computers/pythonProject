from matplotlib import pyplot as plt
import numpy as np
import math
x = np.arange(1, 11)
y = []
for i in range(1, 11):
    y.append(math.sqrt(1 + math.e**math.sqrt(i)+math.cos(i**2))/(abs(1-3*(math.sin(i)**3))) + math.log(abs(2*i)))
plt.grid()
plt.plot(x, y)
plt.show()
half = y[:len(y) // 2]
x2 = np.arange(1, 6)
fig, ax = plt.subplots()
ax.scatter(x2, half)
plt.show()