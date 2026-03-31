def all_divisors(n):
    i =1 
    while(i<=n/2):
        if(n%i==0): print(i)
        i+=i
all_divisors(36)