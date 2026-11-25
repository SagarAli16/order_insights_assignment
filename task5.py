
import pandas as pd

# Load the original dataset
df = pd.read_csv("data/orders_raw.csv")

# Create a copy of the original DataFrame
cleaned_df = df.copy()

# Remove extra spaces
cleaned_df["region"] = cleaned_df["region"].str.strip()
cleaned_df["category"] = cleaned_df["category"].str.strip()

# Convert columns into correct data types
cleaned_df["order_date"] = pd.to_datetime(
    cleaned_df["order_date"], errors="coerce"
)

cleaned_df["quantity"] = pd.to_numeric(
    cleaned_df["quantity"], errors="coerce"
)
cleaned_df["unit_price"] = pd.to_numeric(
    cleaned_df["unit_price"], errors="coerce"
)
cleaned_df["order_value"] = pd.to_numeric(
    cleaned_df["order_value"], errors="coerce"
)

# Remove duplicate rows
cleaned_df = cleaned_df.drop_duplicates()

# Remove records with missing essential order details
cleaned_df = cleaned_df.dropna(
    subset=[
        "order_id",
        "order_date",
        "region",
        "category",
        "quantity",
        "unit_price",
        "order_value",
        "status"
    ]
)

# Keep only positive values
cleaned_df = cleaned_df[
    (cleaned_df["quantity"] > 0) &
    (cleaned_df["unit_price"] > 0) &
    (cleaned_df["order_value"] > 0)
]

# Display the cleaned data
print("Cleaned Data:")
print(cleaned_df.head())

print("\nRows Before Cleaning:", len(df))
print("Rows After Cleaning:", len(cleaned_df))
print("Rows Removed:", len(df) - len(cleaned_df))

print("\nMissing Values After Cleaning:")
print(cleaned_df.isnull().sum())
