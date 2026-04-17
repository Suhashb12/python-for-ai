"""
Functions without return
-----------------------------------------------------------------------------------------
Functions without explicit return statements return None:
"""

def greet(name):
    print(f"Hello, {name}!")
    # No return statement

result = greet("Alice")  # Prints: Hello, Alice!
print(result)  # None