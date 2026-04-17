"""
Parameters
Pass data into your functions
------------------------------------------------------------------------------------------

What are parameters?
Parameters let you pass data into functions. Instead of hardcoding values, you make functions flexible to work with different inputs.
"""
# Without parameters (inflexible)
def greet_alice():
    print("Hello, Alice!")

greet_alice()  # Only works for Alice


# With parameters (flexible)
def greet(name):
    print(f"Hello, {name}!")

# Now it works for anyone
greet("Alice")
greet("Bob")
greet("Charlie")