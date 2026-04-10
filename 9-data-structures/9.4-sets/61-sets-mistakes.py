"""
Common mistakes
"""

"""Empty set syntax"""
# Wrong - creates empty dict
empty = {}

# Right - use set()
empty = set()

"""Sets are unordered"""
# Order is not guaranteed!
numbers = {3, 1, 4, 1, 5}
print(numbers)  # Could be any order

# Use list if order matters
ordered = [3, 1, 4, 1, 5]