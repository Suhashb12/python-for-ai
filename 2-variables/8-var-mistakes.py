""" Forgetting quotes around text """
# Wrong
name = Alice  # Python looks for a variable called Alice

# Right
name = "Alice"  # This creates text



""" Using undefined variables """
# Wrong
print(score)  # Error: score doesn't exist yet
score = 10

# Right
score = 10
print(score)  # Now it works



""" Confusing = and == """
# = means "store"
age = 25

# == means "compare" (we'll learn this later)
if age == 25:
    print("Quarter century!")
