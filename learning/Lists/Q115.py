arr = [1,2,3,4,5,6,7,7,8]
nums = [6,7,7,8,8,9,10]
res = []
for i in arr:
    if i in nums and i not in res:
        res.append(i)
print(res)