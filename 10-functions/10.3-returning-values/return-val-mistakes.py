"""
Common mistakes
"""

"""Forgetting to return"""
# Wrong - calculates but doesn't return
def calculate_total(items):
    total = sum(items)
    # Forgot return!

# Right
def calculate_total(items):
    total = sum(items)
    return total

---------------------------------------------------------------------------

"""Code after return"""
# Wrong - code after return never runs
def get_status():
    return "Done"
    print("This never prints!")  # Unreachable

# Right - return last
def get_status():
    print("Checking status...")
    return "Done"

---------------------------------------------------------------------------

"""Printing instead of returning"""
# Wrong - prints instead of returning
def multiply(a, b):
    print(a * b)

result = multiply(3, 4)  # Prints 12
total = result + 10      # Error! result is None

# Right - return the value
def multiply(a, b):
    return a * b