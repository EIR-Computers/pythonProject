import numpy as np
import random
A = np.arange(27).reshape(3,3,3)
for i in range(3):
    for j in range(3):
        for k in range(3):
            A[i][j][k] = random.randint(0,100)
print(A)