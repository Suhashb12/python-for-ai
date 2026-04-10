"""
Creating sets
You can create sets two ways: with set() or with curly braces {} (but only when it has values).
"""

# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}


# Use set() for empty sets, not {}. Empty curly braces create a dictionary!