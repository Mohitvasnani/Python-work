
def count_digits(n):
    count =0
    while(n>0):
        digit = n%10
        n=n//10
        count+=1
    return count  
def armstrong_num(n):
    count = count_digits(n)
    sum =0
    temp = n
    while(temp>0):
        digit = temp%10
        sum = sum + digit**count
        temp = temp//10
    return sum == n
print(armstrong_num(153))