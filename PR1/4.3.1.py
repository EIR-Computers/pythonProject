from matplotlib import pyplot as plt
import numpy as np
import math

random_float_array = np.random.rand(1, 100)
print(random_float_array)
print("Mean:")
print(np.mean(random_float_array))
print("Median:")
print(np.median(random_float_array))
x = np.arange(0, 100, 1)
fig, ax = plt.subplots()
ax.scatter(x, y=random_float_array)
plt.show()