"""
Default values
-----------------------------------------------------------------------------------------
Give parameters default values for optional arguments:
"""
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Use default
greet("Alice")           # Hello, Alice!

# Override default
greet("Bob", "Hi")       # Hi, Bob!
greet("Charlie", "Hey")  # Hey, Charlie!

"""Put parameters with defaults at the end. Required parameters come first, optional ones last."""