def isarm(n):
    power = countdigit(n)
    sum =0
    temp = n
    while n>0:
        digit = temp % 10
        sum = sum + (digit**power)
        temp = temp//10
    if sum==n:
        return 1

def countdigit(n):
    count=0
    while n>0:
        n =n // 10
        count+=1
    return count