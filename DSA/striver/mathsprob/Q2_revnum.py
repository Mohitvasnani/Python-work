num=2345
def revnum(n):
    rev=0
    while(n>0):
        d = n%10

        rev =  rev *10 + d
        n= n//10

    return rev
print(revnum(num))

