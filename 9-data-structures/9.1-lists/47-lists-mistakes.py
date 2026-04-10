"""
Common mistakes
"""

"""Index out of range"""
# Wrong
fruits = ["apple", "banana"]
print(fruits[2])  # IndexError!

# Right - check length first
if len(fruits) > 2:
    print(fruits[2])

"""Modifying while looping"""
# Wrong - changes list size during loop
numbers = [1, 2, 3, 4]
for num in numbers:
    if num == 2:
        numbers.remove(num)  # Dangerous!

# Right - use list comprehension
numbers = [num for num in numbers if num != 2]

"""Shallow copy issues"""
# Wrong - both variables point to same list
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  # [1, 2, 3, 4] - changed!

# Right - make a copy
list1 = [1, 2, 3]
list2 = list1.copy()
list2.append(4)
print(list1)  # [1, 2, 3] - unchanged