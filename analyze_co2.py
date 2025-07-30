import pandas as pd

# Load dataset
df = pd.read_csv('co2_emissions_tonnes_per_person.csv')

# Simple cleaning
df = df.dropna()
df = df[df['Year'] >= 2000]

# Save cleaned data
df.to_excel('co2_cleaned.xlsx', index=False)

print("Excel file created: co2_cleaned.xlsx")
