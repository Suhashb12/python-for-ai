"""
Common mistakes
"""

"""KeyError when key doesn't exist"""
# Wrong
person = {"name": "Alice"}
print(person["age"])  # KeyError!

# Right - use get()
print(person.get("age", 0))  # Returns 0 if missing

"""Using mutable keys"""
# Wrong - lists can't be keys
bad_dict = {[1, 2]: "value"}  # TypeError!

# Right - use immutable types
good_dict = {(1, 2): "value"}  # Tuple is OK
good_dict = {"1,2": "value"}   # String is OK