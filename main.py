# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.

x = 5 >= 2
A = {1, 3, 7, 8}
B = {2, 4, 5, 10, 'apple'}
C = A & B
df = 'Антонова Антонина', 34, 'ж'
z = 'type'
D = [1, 'title', 2, 'content']
print("Type of x: ", type(x), '\n', "Type of A: ", type(A), '\n', "Type of B: ", type(B), '\n',
      "Type of C: ", type(C), '\n', "Type of df: ", type(df), '\n', "Type of z: ", type(z), '\n',
      "Type of D: ", type(D), '\n')
inp2 = input("Enter number to compare: ")
inp = int(inp2)
if inp < -5:
    print("input value is less then -5")
elif ((inp >= -5) and (inp <= 5)):
    print("input value is between -5 and 5")
else:
    print("input value is more then 5")

a = 10
while a >= 1:
    print(a)
    a -= 3
characteristics = ['height', 'weight', 'age']
for characteristic in characteristics:
    print(characteristic)
list_int = range(2, 15, 1)
for i in range(106, 5, -25):
    print(i)
