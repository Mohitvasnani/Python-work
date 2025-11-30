arr = [5,1,4,4,5,1,23,34,5,3,44,4,34,5,2,3,2,3,23,4,6,89,2,83,5,89]
n = len(arr)
sum = 0
for i in arr:
    sum = sum +i
avg = sum//n
print(avg)