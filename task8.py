

import pandas as pd

# Load original dataset
df = pd.read_csv("data/orders_raw.csv")


# Cleaning function
def clean_orders(df):
    cleaned_df = df.copy()

    # Remove extra spaces and standardize capitalization
    cleaned_df["region"] = cleaned_df["region"].str.strip().str.title()
    cleaned_df["category"] = cleaned_df["category"].str.strip().str.title()

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

    # Remove records with missing essential details
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

    return cleaned_df


# Get cleaned data
cleaned_df = clean_orders(df)


# 1. Mean, Median, and Standard Deviation
print("Order Value Statistics:")
print("Mean:", cleaned_df["order_value"].mean())
print("Median:", cleaned_df["order_value"].median())
print("Standard Deviation:", cleaned_df["order_value"].std())


# 2. Total Sales by Region
print("\nTotal Sales by Region:")
print(cleaned_df.groupby("region")["order_value"].sum())


# 3. Orders by Category
print("\nOrders by Category:")
print(cleaned_df["category"].value_counts())


# 4. Region vs Category
print("\nRegion vs Category:")
print(pd.crosstab(cleaned_df["region"], cleaned_df["category"]))

print("\nOrders by Category:")
print(cleaned_df["category"].value_counts().to_string())