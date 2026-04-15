"""
Best practice: Use parameters and returns
# Bad - using global variable
"""

total = 0

def add_to_total(amount):
    global total
    total += amount

# Good - using parameters and return
def add_amounts(current_total, amount):
    return current_total + amount

total = 0
total = add_amounts(total, 10)
total = add_amounts(total, 20)
print(total)  # 30

"""
When a local and global variable have the same name, the local variable “shadows” the global one inside the function. Python always uses the local version first.
"""