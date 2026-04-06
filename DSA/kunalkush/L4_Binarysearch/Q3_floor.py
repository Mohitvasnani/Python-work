def binarysearch(arr, target):
    start = 0
    end = len(arr)-1
    while(start<=end):
        mid = (start + (end - start) // 2)
        if(target == arr[mid]):
            return arr[mid]
        elif (target > arr[mid]):
                start = mid + 1
        elif target<arr[mid]:
                end =mid-1
    return arr[end]


nums=[1,3,5,7,9,11,13,15,20]
print(binarysearch(nums,12))