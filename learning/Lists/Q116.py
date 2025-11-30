arr = [5,1,4,4,5,1,23,34,5,3,44,4,34,5,2,3,2,3,23,4,6,89,2,5,89,4,4,4,4]

largest = second =0
for i in arr:
    if i > largest:
        second = largest
        largest = i
    elif i>second and i!= largest:
        second = i 
print(second)
