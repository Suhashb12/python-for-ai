"""
Common mistakes
"""

"""Forgetting the colon"""
# Wrong - missing colon
for i in range(5)
    print(i)

# Right - colon after the loop line
for i in range(5):
    print(i)

"""Wrong indentation"""
# Wrong - not indented
for i in range(3):
print(i)

# Right - indented inside the loop
for i in range(3):
    print(i)

"""Off-by-one errors"""
# Wrong - only goes to 4
for i in range(5):
    print(f"Item {i}")  # 0, 1, 2, 3, 4

# Right - if you want 1-5
for i in range(1, 6):
    print(f"Item {i}")  # 1, 2, 3, 4, 5