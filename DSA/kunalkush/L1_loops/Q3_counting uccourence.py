num =int(input("enter"))
tar = int(input("tar"))
count =0
while(num>0):
    digit = num%10
    if digit == tar:
        count+=1
    num = num//10

print (count)
