
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Dashboard title
st.title("Order Insights Dashboard")

# Load cleaned dataset
cleaned_df = pd.read_csv("output/cleaned_orders.csv")

# Total Orders KPI
total_orders = len(cleaned_df)

st.metric("Total Orders", total_orders)

# Region filter
regions = ["All"] + sorted(cleaned_df["region"].unique().tolist())

selected_region = st.selectbox(
    "Select Region",
    regions
)

# Filter data
if selected_region == "All":
    filtered_df = cleaned_df
else:
    filtered_df = cleaned_df[
        cleaned_df["region"] == selected_region
    ]

# Sales chart
st.subheader("Sales by Region")

sales_by_region = filtered_df.groupby("region")["order_value"].sum()

fig, ax = plt.subplots(figsize=(8, 5))

sns.barplot(
    x=sales_by_region.index,
    y=sales_by_region.values,
    ax=ax
)

ax.set_xlabel("Region")
ax.set_ylabel("Total Sales")
ax.set_title("Total Sales by Region")

st.pyplot(fig)
plt.close(fig)

# Filtered data table
st.subheader("Filtered Order Data")
st.dataframe(filtered_df)
