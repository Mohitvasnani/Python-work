# ### 🏋️ Mini Exercises

# **Exercise 1:** Write a recursive function `power(base, exp)` that computes `base ** exp` without using Python's `**` operator.
# ```
# power(2, 0) → 1
# power(2, 3) → 8
# power(3, 4) → 81

# ```

def power(base,exp):
    if exp ==0:
        return 1 
    else:
        return base * power(base,exp-1)
    
print(power(2,3))

# **Exercise 2:** Write a recursive function `reverse_string(s)` that reverses a string.
# ```
# reverse_string("hello") → "olleh"
# reverse_string("abc")   → "cba"

def rev_str(sen):
    if len(sen) ==0:
        return sen
    else:
        return rev_str(sen[1:])+ sen[0]

print(rev_str("hello"))

