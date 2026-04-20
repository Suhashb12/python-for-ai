"""
Common mistakes
"""

"""
Import errors
"""
# Wrong - package not installed or venv not activated
import pandas  # ModuleNotFoundError

# Right - install first
# Run: pip install pandas
import pandas


"""
Name conflicts
"""
# Wrong - overwrites built-in
import datetime
datetime = "2024-01-01"  # Now module is gone!

# Right - use different names
import datetime
date_string = "2024-01-01"