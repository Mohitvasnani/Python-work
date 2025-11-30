print("start comparing the numbers")
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))
max = a
if(max<b):
    max=b
if(max<c):
    max = c
print(max)