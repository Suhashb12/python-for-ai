"""
Common mistakes
"""

"""Forgetting the f in f-strings"""
# Wrong
name = "Alice"
message = "Hello {name}"  # Prints: "Hello {name}"

# Right
message = f"Hello {name}"  # Prints: "Hello Alice"

"""Wrong quotes in strings"""
# Wrong - mismatched quotes
text = 'It's Python'

# Right - escape or use different quotes
text = "It's Python"  # Double quotes outside
text = 'It\'s Python'  # Escape the apostrophe