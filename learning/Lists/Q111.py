arr = [5,1,4,4,5,1,23,34,5,3,44,4,34,5,2,3,2,3,23,4,6,89,2,83,5,89]
n = int(input("Enter a number: "))

found = False
for i in range(len(arr)):
    if arr[i] == n:
        print("Found at index:", i)
        found = True

if not found:
    print("-1 (Not found)")