
import pandas as pd

# Load the original dataset
df = pd.read_csv("data/orders_raw.csv")

# 1. Check missing values
print("Missing Values:")
print(df.isnull().sum())

# 2. Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# 3. Display unique regions
print("\nUnique Regions:")
print(df["region"].unique())

# 4. Display unique categories
print("\nUnique Categories:")
print(df["category"].unique())
