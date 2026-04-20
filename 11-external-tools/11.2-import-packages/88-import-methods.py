"""
Import methods
Different ways to import:
"""
# Import entire module
import math
result = math.sqrt(16)

# Import specific functions
from math import sqrt, pi
result = sqrt(16)
circle_area = pi * radius ** 2

# Import with alias
import pandas as pd
df = pd.DataFrame(data)

# Import everything (avoid this!)
from math import *
"""
Avoid from module import * as it can cause naming conflicts and makes code harder to understand.
"""