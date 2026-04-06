def lsearch2d(matx,target):
    for r in range(len(matx)):
        for c in range(len(matx[r])):
            if matx[r][c]==target:
                return [r,c]
    return -1

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(lsearch2d(matrix,5))