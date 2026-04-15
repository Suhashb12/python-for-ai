"""
Common mistakes
"""
"""
Forgetting parentheses when calling
"""
# Wrong - this doesn't call the function
greet

# Right - parentheses are required
greet()


"""
Forgetting the colon
"""
# Wrong
def greet()
    print("Hello")

# Right
def greet():
    print("Hello")


"""
Bad indentation
"""
# Wrong - not indented
def greet():
print("Hello")

# Right - must indent function body
def greet():
    print("Hello")
