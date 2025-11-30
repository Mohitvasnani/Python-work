arr =[1,105,2,39,37,47,2,32,54,65,60,10,11]
odd = []
even = []
for i in arr:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)
