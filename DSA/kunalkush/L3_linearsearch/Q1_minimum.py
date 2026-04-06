def findmin(arr):
    m = arr[0]
    for a in arr:
        if a<m:
            m = a
    return m

nums =[ 2,3,4,510,1]
print(findmin(nums))