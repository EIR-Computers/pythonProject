import numpy as np
A = np.arange(64).reshape(8, 8)
flag = True;
for i in range(8):
    for j in range(8):
        if(flag == True):
            A[i][j] = 1;
        if (flag == False):
            A[i][j] = 0;
        flag = not(flag)
    flag = not(flag)

print(A)


