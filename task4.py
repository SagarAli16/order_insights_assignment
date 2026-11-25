
import pandas as pd

# Load the original dataset
df = pd.read_csv("data/orders_raw.csv")

# Create a copy of the original DataFrame
cleaned_df = df.copy()

# Remove extra spaces from region and category
cleaned_df["region"] = cleaned_df["region"].str.strip()
cleaned_df["category"] = cleaned_df["category"].str.strip()

# Convert order_date into datetime format
cleaned_df["order_date"] = pd.to_datetime(
    cleaned_df["order_date"], errors="coerce"
)

# Convert columns into numeric format
cleaned_df["quantity"] = pd.to_numeric(
    cleaned_df["quantity"], errors="coerce"
)
cleaned_df["unit_price"] = pd.to_numeric(
    cleaned_df["unit_price"], errors="coerce"
)
cleaned_df["order_value"] = pd.to_numeric(
    cleaned_df["order_value"], errors="coerce"
)

# Display the cleaned data
print("Cleaned Data:")
print(cleaned_df.head())

print("\nData Types After Cleaning:")
print(cleaned_df.dtypes)
