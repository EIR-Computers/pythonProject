import numpy as np
import random
A = np.arange(25).reshape(5, 5)
for i in range(5):
    for j in range(5):
        A[i][j] = random.randint(0,4)
print(A)