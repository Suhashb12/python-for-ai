"""
Booleans
True and False values for decisions

​
What are booleans?
Booleans are the simplest data type - they can only be True or False. Think of them as yes/no answers.
"""

is_logged_in = True
is_admin = False
has_permission = True

"""Boolean values are True and False with capital letters. Using true or false will cause an error! """

"""
Creating booleans

Booleans often come from comparisons:
"""
# Direct assignment
is_ready = True

# From comparisons
age = 18
can_vote = age >= 18  # True

score = 75
passed = score > 60   # True

""" 
Comparison operators 

These operators compare values and return True or False:
"""
age = 25

# Equality
print(age == 25)     # True - equals
print(age != 30)     # True - not equals

# Greater/Less than
print(age > 20)      # True - greater than
print(age < 30)      # True - less than
print(age >= 25)     # True - greater or equal
print(age <= 25)     # True - less or equal

#  Remember: = assigns a value, while == compares values. This is a common source of bugs!
​
"""-------------------------------------------------------------------------"""
"""Common mistakes """
"""Wrong capitalization"""
# Wrong
is_ready = true   # NameError!
is_done = TRUE    # NameError!

# Right
is_ready = True
is_done = False

"""Using = instead of =="""
# Wrong - this assigns, not compares!
if is_logged_in = True:
    print("Welcome")

# Right - but redundant
if is_logged_in == True:
    print("Welcome")
    
# Best - booleans are already True/False
if is_logged_in:
    print("Welcome")