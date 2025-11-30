arr = [5,1,4,4,5,1,23,34,5,3,44,4,34,5,2,3,2,3,23,4,6,89,2,83,5,89,4,4,4,4]
max = 0 
for i in arr:
    if(arr.count(i)>max):
        max = i
print(max)

result = []
for i in arr:
    if i not in result:
        result.append(i)
for i in result:
    count = arr.count(i)
    print(f"{i} is {count}")