
import pandas as pd
import os

# Cleaning function
def clean_orders(df):
    cleaned_df = df.copy()

    cleaned_df["region"] = cleaned_df["region"].str.strip()
    cleaned_df["category"] = cleaned_df["category"].str.strip()

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

    cleaned_df = cleaned_df.drop_duplicates()

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

    cleaned_df = cleaned_df[
        (cleaned_df["quantity"] > 0) &
        (cleaned_df["unit_price"] > 0) &
        (cleaned_df["order_value"] > 0)
    ]

    return cleaned_df


# Load original dataset
df = pd.read_csv("data/orders_raw.csv")

# Count rows before cleaning
rows_before = len(df)

# Clean the dataset
cleaned_df = clean_orders(df)

# Count rows after cleaning
rows_after = len(cleaned_df)

# Calculate removed rows
rows_removed = rows_before - rows_after

# Create quality report
quality_report = pd.DataFrame({
    "Metric": [
        "Rows Before Cleaning",
        "Rows After Cleaning",
        "Rows Removed"
    ],
    "Count": [
        rows_before,
        rows_after,
        rows_removed
    ]
})

# Create output folder
os.makedirs("output", exist_ok=True)

# Save quality report
quality_report.to_csv(
    "output/data_quality_report.csv",
    index=False
)

# Display report
print("Data Quality Report:")
print(quality_report)

print("\nReport saved successfully!")
