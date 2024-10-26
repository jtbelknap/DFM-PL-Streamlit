import streamlit as st
import pandas as pd

st.title("Profit & Loss Model with Manufacturing Tracker")

# Step 1: Enter product line details (costs, COGS, etc.)
st.header("Product Line Details (Fixed Costs)")
st.subheader("Enter the product line data once.")

# Input product line details
labor_cost = st.number_input("Labor Cost per Unit", min_value=0.0, value=0.0, key="labor_cost")
cogs = st.number_input("COGS per Unit", min_value=0.0, value=0.0, key="cogs")
marketing_cost = st.number_input("Marketing Cost per Unit", min_value=0.0, value=0.0, key="marketing_cost")
unit_price = st.number_input("Unit Sale Price", min_value=0.0, value=0.0, key="unit_price")

# Step 2: Enter monthly unit sales volumes
st.header("Monthly Unit Sales Volume")
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

monthly_sales = {}
for month in months:
    monthly_sales[month] = st.number_input(f"{month} Sales Volume", min_value=0, value=0, key=f"sales_{month}")

# Step 3: Calculate monthly subtotals
st.header("Monthly Subtotals")

# Create a DataFrame to display monthly calculations
data = {
    "Month": months,
    "Units Sold": [monthly_sales[month] for month in months],
    "Revenue": [monthly_sales[month] * unit_price for month in months],
    "Labor Cost": [monthly_sales[month] * labor_cost for month in months],
    "COGS": [monthly_sales[month] * cogs for month in months],
    "Marketing": [monthly_sales[month] * marketing_cost for month in months],
}

df = pd.DataFrame(data)
df["Gross Profit"] = df["Revenue"] - (df["Labor Cost"] + df["COGS"] + df["Marketing"])

# Display the DataFrame with monthly calculations
st.dataframe(df)

# Step 4: Display Yearly Totals
st.header("Yearly Totals")

total_revenue = df["Revenue"].sum()
total_labor_cost = df["Labor Cost"].sum()
total_cogs = df["COGS"].sum()
total_marketing = df["Marketing"].sum()
total_gross_profit = df["Gross Profit"].sum()

st.write(f"**Total Revenue:** ${total_revenue}")
st.write(f"**Total Labor Cost:** ${total_labor_cost}")
st.write(f"**Total COGS:** ${total_cogs}")
st.write(f"**Total Marketing Cost:** ${total_marketing}")
st.write(f"**Total Gross Profit:** ${total_gross_profit}")
