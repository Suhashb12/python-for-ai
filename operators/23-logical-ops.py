"""
These combine boolean values and conditions:
"""
age = 25
has_license = True
drunk = True

# AND - both must be true
can_drive = age >= 16 and has_license
print(can_drive)  # True

can_drive = age >= 16 and has_license and not drunk
print(can_drive)  # False
# OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)  # True

# NOT - reverses the value
is_adult = age >= 18
is_child = not is_adult
print(is_child)  # False