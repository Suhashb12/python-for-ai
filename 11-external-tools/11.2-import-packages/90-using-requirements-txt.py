"""Sharing your project: requirements.txt
When you share your Python project, others need to know which packages to install. The standard way is using a requirements.txt file:
"""

"""
Creating requirements.txt
List all your project’s packages:
"""
pip freeze > requirements.txt
"""
This creates a file like:
"""
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.0

"""
Installing from requirements.txt
When someone gets your project, they run:
"""
pip install -r requirements.txt

"""
This installs all the packages at once!
Later in the course, we’ll learn about uv - a modern, faster alternative to pip that makes package management even easier.
"""