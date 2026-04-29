"""
Load into pandas
-------------------------------------------------------------------------------------------
Now let's organize this data:
"""
import pandas as pd

# Extract the daily data
daily_data = data['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)

"""
Output:
        date  max_temp  min_temp
0 2024-01-08      12.3       5.1
1 2024-01-09      11.8       4.2
2 2024-01-10      13.5       6.0
...
"""