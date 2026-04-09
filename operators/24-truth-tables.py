"""
Understanding how and, or, and not work:
"""
# AND: Both must be True
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False
print(False and True)   # False

# OR: At least one must be True  
print(True or False)    # True
print(False or False)   # False
print(True or True)     # True
print(False or True)    # True

# NOT: Flips the value
print(not True)         # False
print(not False)        # True