# Exercise 1: Write a loop that prints all numbers from 1 to 20 that are divisible by 3.

for i in range(2, 20):
    if(i%3==0):
        print(i)


str = "programming"

def num_vowels(string):
    count = 0
    for ch in string:
        if ch == 'a' or ch == 'e' or ch=='i' or ch=='o' or ch=='u':
            count = count + 1
    return count

print(num_vowels(str))
             