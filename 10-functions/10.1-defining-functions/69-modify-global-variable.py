
"""
Modifying global variables
To change a global variable inside a function, use the global keyword:
"""

counter = 0  # Global variable

def increment():
    global counter  # Declare we want to modify the global variable
    counter += 1

increment()
increment()
print(counter)  # 2

"""
Avoid using global when possible. It makes code harder to understand and debug. Instead, pass values as parameters and return results.
"""