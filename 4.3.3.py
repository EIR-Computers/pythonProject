from matplotlib import pyplot as plt
from numpy import trapz
import numpy as np
import math
x = np.arange(0, 10)
y = []
for i in range(1, 11):
    y.append(abs(math.cos(i*math.e**(math.cos(i) + math.log(i + 1)))))
plt.grid()
plt.plot(x, y)
plt.fill_between(x, y)
area = trapz(y)
plt.show()
print(area)