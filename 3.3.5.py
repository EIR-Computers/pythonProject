x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
a = []
while i < 10:
    a.append(i)
    i += 2
b = a[::-1]
i = 0
d = []
c1 = 0
c2 = 0
while i < 10:
    if i % 2 == 0:
        x[i] = b[c1]
        c1 += 1

    i += 1

for i in range(10):
    print(x[i])

