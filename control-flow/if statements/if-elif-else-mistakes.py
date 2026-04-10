"""
Common mistakes
"""

"""Forgetting the colon"""
# Wrong
if x > 5
    print("Big")

# Right
if x > 5:
    print("Big")


"""Using = instead of =="""
# Wrong (assignment)
if x = 5:
    print("Five")

# Right (comparison)
if x == 5:
    print("Five")

"""Wrong indentation"""
# Wrong
if True:
print("Hello")  # IndentationError

# Right
if True:
    print("Hello")