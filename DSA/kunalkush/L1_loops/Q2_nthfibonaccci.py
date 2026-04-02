num = int(input("enter num:"))

def fib(num):
     s =0
     e =1
     count = 2
     while num>=count:
         temp = e
         e = e + s
         s = temp
         count +=1
     return e

print(fib())

