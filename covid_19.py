import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('WHO_Covid19_Dataset.csv')

# 1. Basic Inspection
print("🔹 First 5 rows:")
print(df.head())

print("\n🔹 Dataset Info:")
print(df.info())

print("\n🔹 Summary Statistics (Numerical Columns):")
print(df.describe())

# 2. Checking for Missing Values
print("\n🔹 Missing Values:")
print(df.isnull().sum())

# 3. Checking for Duplicates
duplicate_rows = df.duplicated()
print(f"\n🔹 Number of Duplicate Rows: {duplicate_rows.sum()}")
df = df.drop_duplicates()

# 4. Convert Date to datetime
df['Date_reported'] = pd.to_datetime(df['Date_reported'])

# 5. Standardizing Text Columns
df['Country'] = df['Country'].str.strip().str.title()
df['WHO_region'] = df['WHO_region'].str.strip().str.upper()

# 6. Check for Inconsistencies
print("\n🔹 Unique WHO Regions:")
print(df['WHO_region'].unique())

# 7. Visualizing Missing Values (Optional but helpful)
import missingno as msno
msno.matrix(df)
plt.title("Missing Data Matrix")
plt.show()

# 8. Handling Missing Country Codes (Optional Handling)
missing_country_codes = df['Country_code'].isnull().sum()
print(f"\n🔹 Missing Country Codes: {missing_country_codes}")

# 9. EDA - Total Cases and Deaths Over Time (Global)
df_grouped = df.groupby('Date_reported').sum(numeric_only=True)

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_grouped, x=df_grouped.index, y='Cumulative_cases')
plt.title('Global Cumulative COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Cumulative Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_grouped, x=df_grouped.index, y='Cumulative_deaths', color='red')
plt.title('Global Cumulative COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Cumulative Deaths')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 10. EDA - Top 10 Countries with Highest Total Cases
latest_data = df[df['Date_reported'] == df['Date_reported'].max()]
top10 = latest_data.sort_values(by='Cumulative_cases', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x='Cumulative_cases', y='Country', data=top10, palette='viridis')
plt.title('Top 10 Countries by Cumulative COVID-19 Cases')
plt.xlabel('Cumulative Cases')
plt.ylabel('Country')
plt.tight_layout()
plt.show()
