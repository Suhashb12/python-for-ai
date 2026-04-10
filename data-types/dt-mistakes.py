"""Common mistakes """
"""Wrong capitalization"""
# Wrong
is_ready = true   # NameError!
is_done = TRUE    # NameError!

# Right
is_ready = True
is_done = False

"""Using = instead of =="""
# Wrong - this assigns, not compares!
if is_logged_in = True:
    print("Welcome")

# Right - but redundant
if is_logged_in == True:
    print("Welcome")
    
# Best - booleans are already True/False
if is_logged_in:
    print("Welcome")