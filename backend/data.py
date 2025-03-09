import pandas as pd

# Define the cost values
weather_costs = {
    'Sunny': 0,
    'Partly Cloudy ': 2,
    'Heavy Rain': 10,
    'Windy': 5,
    'Moderate Rain': 7,
    'Mostly Cloudy ': 5,
    'Fog': 10,
    'Thunderstorms': 15,
    'Hail': 15,
    'Light Snow ': 6,
    'Moderate Snow ': 9,
    'Heavy Snow': 10,
    'Light Rain': 5
}

time_costs = {
    'Morning Rush Hour ': 10,
    'Midday ': 3,
    'Evening Rush Hour': 10,
    'Night': 0
}

day_costs = {
    'Weekday ': 0,
    'Weekend ': 5,
    'Holiday ': 8
}

# Read the CSV file
df = pd.read_csv('dataset ml - Sheet1.csv')

# Update the Cost column
df['Cost'] = df.apply(lambda row: weather_costs[row['Weather ']] + time_costs[row['Time']] + day_costs[row['Day']], axis=1)

# Save the updated CSV file
df.to_csv('data_updated.csv', index=False)

print("Costs updated successfully and saved to data_updated.csv")

