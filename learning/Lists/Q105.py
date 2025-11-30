arr =[1,105,2,39,37,47,2]
n = int(input("old number"))
x = int(input("new number"))
for i in range(0,len(arr)):
    if(arr[i]==n):
        arr.remove(arr[i])
        arr.insert(i,x)
        break
print("updated array", arr)