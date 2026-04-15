"""
Variable scope: Local vs Global
Variables in Python have a “scope” - where they can be accessed and used.
"""
"""
Local variables
Variables created inside a function only exist within that function:
"""

def calculate_price():
    price = 100
    tax = price * 0.1
    print(f"Total: {price + tax}")

calculate_price()  # Total: 110

# This fails - price doesn't exist outside the function
print(price)  # NameError: name 'price' is not defined​
