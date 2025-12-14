#truthy and falsy values in Python
# In Python, certain values are considered "truthy" or "falsy" when evaluated in a boolean context.
# Falsy values include:
# - None
# - False
# - 0 (integer zero)        
# - 0.0 (float zero)
# - "" (empty string)
# - [] (empty list)
# - {} (empty dictionary)
# - () (empty tuple)
# - set() (empty set)
# All other values are considered truthy.
# Here are some examples:
if []:
    print("This list is truthy")

if [1, 2, 3]:
    print("This list is truthy")
arr = []
if not arr:
    print("The list is empty")  