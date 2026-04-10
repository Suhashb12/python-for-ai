"""
Combine conditions with and, or, not:
"""

age = 25
has_license = True

# Both must be True
if age >= 18 and has_license:
    print("You can drive!")

# At least one must be True
if weekend or holiday:
    print("No work today!")

# Reverse the condition
if not raining:
    print("Let's go outside!")
