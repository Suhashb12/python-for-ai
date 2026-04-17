"""
Return vs print
-----------------------------------------------------------------------------------------
Understanding the difference is crucial:
"""
def get_greeting_print(name):
    print(f"Hello, {name}!")  # Just displays

def get_greeting_return(name):
    return f"Hello, {name}!"  # Gives back value

# Can't use print version's output
message = get_greeting_print("Alice")  # Prints but returns None
print(message)  # None

# Can use return version's output
message = get_greeting_return("Alice")  # Returns the string
print(message.upper())  # HELLO, ALICE!

"""
Use return when you need to use the result elsewhere. Use print when you just want to display information.
"""