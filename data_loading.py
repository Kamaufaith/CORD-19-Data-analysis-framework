# Part 1: Data Loading and Initial Exploration
import pandas as pd
# Load the dataset
try:
    df = pd.read_csv("~/Downloads/metadata.csv")
    print("Data loaded successfully")
except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print(f"An error occured: {e}")
df.head()
# Display the number of rows and columns
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")
# Display the data types of each column
print("\nData Types:")
print(df.dtypes)
# check for missing values in each column
missing_values = df.isnull().sum()
print("\nMissing Values:")
print(missing_values[missing_values > 0])
# Generate descriptive statistics for numerical columns
print("\nDescriptive Statistics for Numerical Columns:")
print(df.describe())
# Checking how many unique values exist for text data
print("\nUnique Journals:", df['journal'].nunique( ))
print("Unique Authors:", df['authors'].nunique())
# Drop rows with missing titles or abstracts, as these are critical for analysis
df_cleaned = df.dropna(subset=['title', 'abstract'])
# Optionally fill missing journal names with 'Unknown'
df_cleaned['journal'].fillna('Unknown', inplace=True)
print(f"\nCleaned dataset shape: {df_cleaned.shape}")
## Summary of part 1 
# loadedthe CORD-19 metadata.csv file into pandas
# inspected structure and previewed data
# checked for missing values
# computed basic descriptive statistics
# cleaned key missing entries
##

#Part 2: Data Cleaning and Preparation

# Check missing values per column
missing_values = df.isnull().sum().sort_values(ascending=False)
print("Missing values per column:\n", missing_values)
# Percentage of missing values
missing_percent = (df.isnull().mean() * 100).sort_values(ascending=False)
print("Percentage of missing values:\n", missing_percent)
# Columns with more than 50% missing values
high_missing = missing_percent[missing_percent > 50]
print("\ncolumns with >50% missing values:\n", high_missing)
# Drop columns with >50% missing values
df_clean = df.drop(columns=high_missing.index)
# Drop rows missing critical fields
df_clean = df_clean.dropna(subset=['title', 'publish_time'])
# Fill less-critical missing values
df_clean['journal'] = df_clean['journal'].fillna('Unknown')
df_clean['abstract'] = df_clean['abstract'].fillna('No abstract provided')
# Convert publish_time to datetime format
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
# Extract publication year
df_clean['publish_year'] = df_clean['publish_time'].dt.year
# Summary after cleaning
print("\nCleaned dataset shape:", df_clean.shape)
print("Remaining missing values:\n", df_clean.isnull().sum())
df_clean.head(5)
# Save the cleaned dataset to a new CSV file
df_clean.to_csv("~/Downloads/cord19_cleaned.csv", index=False)
print("Cleaned dataset saved to Downloads as 'cord19_cleaned.csv'")