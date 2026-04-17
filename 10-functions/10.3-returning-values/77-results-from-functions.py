"""
Return values
----------------------------------------------------------------------------------------
Get results back from your functions

-----------------------------------------------------------------------------------------
Getting results from functions
So far, our functions have printed output. But often you want functions to calculate something and give you the result to use elsewhere.
"""
# This function only prints
def add_print(a, b):
    print(a + b)

# This function returns a value
def add_return(a, b):
    return a + b

# Now you can use the result
result = add_return(5, 3)
print(f"The result is {result}")  # The result is 8



def add_print(a, b):
    print(a + b)

result = add_print(15, 3)  # Prints 8

result() # 'NoneType' object is not callable


def add_print(a, b):
    return a + b
result = add_print(15, 3)  # Returns 18