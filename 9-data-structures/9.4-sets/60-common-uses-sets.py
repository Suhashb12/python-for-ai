"""
Common uses
"""

"""Remove duplicates"""
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(set(names))
print(unique_names)  # ['Alice', 'Bob', 'Charlie']


"""Fast membership testing"""
allowed_users = {"alice", "bob", "charlie"}

if "alice" in allowed_users:  # Very fast!
    print("Access granted")