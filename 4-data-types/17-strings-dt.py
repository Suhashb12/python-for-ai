"""
Strings
Working with text in Python

​
What are strings?
Strings are text - any characters inside quotes. Python doesn’t care if you use single or double quotes, just be consistent.
"""
name = "Alice"
message = 'Hello, World!'

"""---------------------------------------------------------------------
Creating strings
Three ways to make strings:"""

# Single quotes
first = 'Python'

# Double quotes  
second = "Python"

# Triple quotes for multiple lines
paragraph = """This is
a multi-line
string"""

"""---------------------------------------------------------------------
Combining strings

Join strings together with +:
"""

first_name = "John"
last_name = "Doe"

# Concatenation
full_name = first_name + " " + last_name
print(full_name)  # John Doe

# Repetition
stars = "*" * 5
print(stars)  # *****""

say = first_name + " " + paragraph + " " + last_name
print(say)

"""---------------------------------------------------------------------
String length

Use len() to count characters:
"""
message = "Hello"
print(len(message))  # 5

empty = ""
print(len(empty))    # 0

len(full_name)
len(stars)
"""---------------------------------------------------------------------
Converting to string

Turn other types into strings with str():
"""

age = 25
message = "I am " + str(age) + " years old"
print(message)  # I am 25 years old

# Or use f-strings (we'll learn more later)
message = f"I am {age} years old"

"""---------------------------------------------------------------------
Common mistakes
"""

""" Mixing quotes """
# Wrong - mismatched quotes
text = "Hello'

# Right - matching quotes
text = "Hello"
text = 'Hello'

""" Can't add strings and numbers """
# Wrong
result = "Age: " + 25  # TypeError!

# Right - convert number first
result = "Age: " + str(25)

""" Forgetting quotes entirely """
# Wrong
name = Alice  # Python looks for variable Alice

# Right  
name = "Alice"  # String literal

"""---------------------------------------------------------------------"""