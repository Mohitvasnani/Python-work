arr =[1,105,2,39,37,47,2]
for i in arr[:]:
    if(i%2!=0):
        arr.remove(i)
print(arr)