"""
The return statement
Use return to send a value back from a function:
"""
def calculate_area(width, height):
    area = width * height
    return area

# Store the returned value
room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sq ft")  # Room size: 120 sq ft

"""
When Python hits a return statement, it immediately exits the function. Any code after return won’t run.
"""