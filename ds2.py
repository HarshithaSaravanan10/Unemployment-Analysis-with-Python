import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:\Users\Harshitha\OneDrive\文档\HARSHY CLG\Unemployment in India.csv"  # Update path if needed
df = pd.read_csv(file_path)

# Remove extra spaces in column names
df.columns = df.columns.str.strip()

# Remove extra spaces in all string columns
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Display basic information about the dataset
print("Dataset Info:")
print(df.info())

# Display first few rows
print("\nFirst 5 Rows:")
print(df.head())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Drop rows with missing values
df.dropna(inplace=True)

# Convert 'Date' column to datetime format after removing spaces
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y", errors="coerce")

# Drop rows where Date conversion failed
df.dropna(subset=["Date"], inplace=True)

# Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# Line plot for unemployment rate over time
plt.figure(figsize=(12, 6))
sns.lineplot(x="Date", y="Estimated Unemployment Rate (%)", data=df, marker="o", color="b")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.title("Trend of Unemployment Rate in India")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Boxplot to compare unemployment rate across regions
plt.figure(figsize=(14, 6))
sns.boxplot(x="Region", y="Estimated Unemployment Rate (%)", data=df)
plt.xticks(rotation=90)
plt.xlabel("Region")
plt.ylabel("Unemployment Rate (%)")
plt.title("Unemployment Rate Distribution by Region")
plt.show()

# Save cleaned dataset
df.to_csv("Cleaned_Unemployment_Data.csv", index=False)
print("Cleaned dataset saved successfully.")
