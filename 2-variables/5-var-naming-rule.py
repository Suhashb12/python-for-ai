# Allowed
user_name = "Dave"     # lowercase with underscores (Python style)
userName = "Dave"      # camelCase (works but not Python style)
age2 = 30              # numbers are OK (not at start)
_private = "secret"    # underscore at start is OK

# Not allowed
2age = 30              # Can't start with number
my-name = "Dave"       # No hyphens (Python thinks it's subtraction)
my name = "Dave"       # No spaces
class = "Python"       # Can't use Python keywords