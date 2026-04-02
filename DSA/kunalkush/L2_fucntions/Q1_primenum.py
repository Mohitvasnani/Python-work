num=int(input(""))
def isprime(num):
    c=2

    while(c*c<=num):
        if num%c==0:
            return False
        c+=1
    return True
