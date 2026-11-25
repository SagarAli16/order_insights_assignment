
import pandas as pd

# Load the dataset
df = pd.read_csv("data/orders_raw.csv")

# Display first five rows
print("First Five Rows:")
print(df.head())

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display data types
print("\nData Types:")
print(df.dtypes)
