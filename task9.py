
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load original dataset
df = pd.read_csv("data/orders_raw.csv")


# Cleaning function
def clean_orders(df):
    cleaned_df = df.copy()

    # Clean region and category
    cleaned_df["region"] = cleaned_df["region"].str.strip().str.title()
    cleaned_df["category"] = cleaned_df["category"].str.strip().str.title()

    # Convert data types
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

    # Remove duplicates
    cleaned_df = cleaned_df.drop_duplicates()

    # Remove missing essential details
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

    # Keep positive values
    cleaned_df = cleaned_df[
        (cleaned_df["quantity"] > 0) &
        (cleaned_df["unit_price"] > 0) &
        (cleaned_df["order_value"] > 0)
    ]

    return cleaned_df


# Get cleaned data
cleaned_df = clean_orders(df)

# Create output folder
os.makedirs("output", exist_ok=True)

# Set Seaborn style
sns.set_style("whitegrid")


# 1. Histogram of Order Values
plt.figure(figsize=(8, 5))

sns.histplot(
    data=cleaned_df,
    x="order_value",
    bins=20
)

plt.title("Distribution of Order Values")
plt.xlabel("Order Value")
plt.ylabel("Number of Orders")

plt.savefig("output/order_value_histogram.png")
plt.show()
plt.close()


# 2. Bar Chart of Sales by Region
sales_by_region = cleaned_df.groupby("region")["order_value"].sum()

plt.figure(figsize=(8, 5))

sns.barplot(
    x=sales_by_region.index,
    y=sales_by_region.values
)

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.savefig("output/sales_by_region.png")
plt.show()
plt.close()


# 3. Scatter Plot: Order Value vs Delivery Days
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=cleaned_df,
    x="delivery_days",
    y="order_value"
)

plt.title("Order Value vs Delivery Days")
plt.xlabel("Delivery Days")
plt.ylabel("Order Value")

plt.savefig("output/order_value_vs_delivery_days.png")
plt.show()
plt.close()


print("All three charts created and saved successfully!")
