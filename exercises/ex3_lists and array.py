# **Exercise 1:** Given a list of numbers, return a new list where each element is doubled. Do it using list comprehension in one line.
# ```

arr = [1,2,3,4,5,6]

doubles = [arr[a]*2 for a in range(0,len(arr))]
print (doubles)

# **Exercise 2 — Two Pointer:** Given a sorted list and a target, find if any two numbers add up to the target. Return True or False.
nums = [1, 3, 5, 7, 9]
target = 12

def searcht(arr, target):
    start = 0
    end = len(arr)-1
    sum =0
    while end>start:
       sum = arr[start] + arr[end]
       if sum==target:
           return True
       elif sum>target:
           end =end-1
       elif sum<target:
           start = start + 1
       else: return False
print(searcht(nums,target))

# **Exercise 3 — Sliding Window:** Given a list and a number k, find the minimum sum of any k consecutive elements.
# ```
# [3, 1, 4, 1, 5, 9, 2, 6], k=3 → 6 (1+4+1 or 1+1+4... wait, trace it yourself!)


arr =[3, 1, 4, 1, 5, 9, 2, 6]
def minsum(arr,k):
    

