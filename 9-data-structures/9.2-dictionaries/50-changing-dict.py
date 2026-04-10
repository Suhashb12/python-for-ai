"""
Changing dictionaries
"""

person = {"name": "Alice", "age": 30}

# Add or update
person["email"] = "alice@email.com"  # Add new
person["age"] = 31                   # Update existing

# Remove items
del person["email"]              # Remove by key
age = person.pop("age")          # Remove and return
person.clear()                   # Remove all items