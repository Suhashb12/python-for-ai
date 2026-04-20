"""
Installing packages
External packages need installation:
"""

# Install a package
pip install requests

# Install specific version
pip install requests==2.28.0

# Install multiple packages
pip install pandas numpy matplotlib

"""
Always ensure your virtual environment is activated before installing! This is the #1 source of import errors. If you get “ModuleNotFoundError” after installing, you probably installed to the wrong environment. Learn more about virtual environments.
"""