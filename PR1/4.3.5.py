import math
inp1 = input("Hello, type A: ")
print('\n')
inp2 = input("Type B: ")
print("Menu \n 1.+ \n 2.- \n 3.* \n 4./ \n 5.f1 = exp(x+y) \n 6.f2 = sin(x+y) \n 7.f3 = cos(x+y) \n 8.f4 = X^Y")
inp3 = input("Selection: ")
if (inp3 == '1'):
    print("ANS: ")
    print(int(inp1) + int(inp2))
if (inp3 == '2'):
    print("ANS: ")
    print(int(inp1) - int(inp2))
if (inp3 == '3'):
    print("ANS: ")
    print(int(inp1) * int(inp2))
if (inp3 == '4'):
    print("ANS: ")
    print(int(inp1) / int(inp2))
if (inp3 == '5'):
    print("ANS: ")
    x = int(inp1)
    y = int(inp2)
    ans = math.exp(x + y)
    print (ans)
if (inp3 == '6'):
    print("ANS: ")
    x = int(inp1)
    y = int(inp2)
    ans = math.sin(x + y)
    print (ans)
if (inp3 == '7'):
    print("ANS: ")
    x = int(inp1)
    y = int(inp2)
    ans = math.cos(x + y)
    print (ans)
if (inp3 == '8'):
    print("ANS: ")
    x = int(inp1)
    y = int(inp2)
    ans = math.pow(x, y)
    print (ans)