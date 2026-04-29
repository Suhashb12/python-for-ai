"""
Understanding the response
------------------------------------------------------------------------------------------
The API sends back data in JSON format (like a Python dictionary):
"""
{
    'latitude': 48.84,
    'longitude': 2.36,
    'timezone': 'GMT',
    'elevation': 46.0,
    'current_units': {
        'temperature_2m': '°C'
    },
    'current': {
        'time': '2025-08-01T08:30',
        'temperature_2m': 20.0
    }
}

"""
The temperature is nested inside current, so to get it:
"""
temperature = data['current']['temperature_2m']
print(f"Temperature in Paris: {temperature}°C")
# Output: Temperature in Paris: 20.0°C


"""
What is JSON? JSON (JavaScript Object Notation) is just a way to structure data, similar to CSV or Excel files. While CSV stores data in rows and columns, JSON uses key-value pairs like Python dictionaries.
"""