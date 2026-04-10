"""
Common mistakes
"""

"""Division always returns float"""
# Regular division
result = 10 / 2    # 5.0 (not 5)

# Integer division
result = 10 // 2   # 5

"""Order of operations"""
# Wrong
average = 10 + 20 + 30 / 3  # 40.0

# Right
average = (10 + 20 + 30) / 3  # 20.0

"""Confusing = and =="""
# = assigns a value
age = 18

# == compares values
if age == 18:
    print("Just turned adult!")