"""
For multiple conditions:
"""


score = 85

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")




"""
Python checks each condition in order and runs the first True one.

Why elif instead of multiple if statements? With elif, Python stops checking once it finds a true condition. This is more efficient and prevents multiple blocks from running. The order matters - always put more specific conditions first!
"""