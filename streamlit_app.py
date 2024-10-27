import streamlit as st
import pandas as pd

st.title("Multi-Product Line Profit & Loss Model")

# Step 1: Enter the number of product lines
st.sidebar.header("Configuration")
num_products = st.sidebar.number_input("Number of Product Lines", min_value=1, value=2, step=1)

# Step 2: Input General Expense (Rent or Other)
st.sidebar.subheader("General Expenses")
general_expense = st.sidebar.number_input("Monthly General Expense (e.g., Rent)", min_value=0.0, value=0.0)

# Step 3: Input product line details
product_data = []
for i in range(num_products):
    st.subheader(f"Product Line {i + 1} Details")
    product_name = st.text_input(f"Product Line {i + 1} Name", key=f"name_{i}")
    unit_price = st.number_input(f"Unit Sale Price ({product_name})", min_value=0.0, value=0.0, key=f"price_{i}")
    labor_cost = st.number_input(f"Labor Cost per Unit ({product_name})", min_value=0.0, value=0.0, key=f"labor_{i}")
    cogs = st.number_input(f"COGS per Unit ({product_name})", min_value=0.0, value=0.0, key=f"cogs_{i}")
    marketing_cost = st.number_input(f"Marketing Cost per Unit ({product_name})", min_value=0.0, value=0.0, key=f"marketing_{i}")
    additional_expenses = st.number_input(f"Additional Monthly Expenses ({product_name})", min_value=0.0, value=0.0, key=f"expenses_{i}")

    product_data.append({
        "name": product_name,
        "unit_price": unit_price,
        "labor_cost": labor_cost,
        "cogs": cogs,
        "marketing_cost": marketing_cost,
        "additional_expenses": additional_expenses
    })

# Step 4: Monthly sales volume input for each product line
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

st.header("Monthly Sales Volume")
monthly_sales = {}

for i, product in enumerate(product_data):
    st.subheader(f"Sales Volume for {product['name']}")
    
    # Checkbox for setting the same value across all months
    same_sales = st.checkbox(f"Same sales units for all months ({product['name']})", key=f"same_sales_{i}")
    
    # Input for sales units (either single input or per month)
    if same_sales:
        units = st.number_input(f"Sales Units for All Months ({product['name']})", min_value=0, value=0, key=f"all_months_{i}")
        monthly_sales[product["name"]] = {month: units for month in months}
    else:
        monthly_sales[product["name"]] = {}
        for month in months:
            key = f"sales_{i}_{month}"
            monthly_sales[product["name"]][month] = st.number_input(
                f"{month} Sales ({product['name']})", min_value=0, value=0, key=key)

# Step 5: Calculate and display monthly and yearly totals
st.header("Monthly Subtotals & Yearly Totals")

# Create a summary DataFrame
summary_data = []
for product in product_data:
    product_name = product["name"]
    for month in months:
        units_sold = monthly_sales[product_name][month]
        revenue = units_sold * product["unit_price"]
        labor_cost = units_sold * product["labor_cost"]
        cogs = units_sold * product["cogs"]
        marketing = units_sold * product["marketing_cost"]

        # Corrected parentheses for gross profit and net profit calculation
        gross_profit = revenue - (labor_cost + cogs + marketing)
        net_profit = gross_profit - product["additional_expenses"] - (general_expense / num_products)

        summary_data.append([
            product_name, month, units_sold, revenue, labor_cost, 
            cogs, marketing, gross_profit, net_profit
        ])

# Convert to DataFrame for display
df = pd.DataFrame(summary_data, columns=[
    "Product Line", "Month", "Units Sold", "Revenue", 
    "Labor Cost", "COGS", "Marketing", "Gross Profit", "Net Profit"])

st.dataframe(df)

# Step 6: Display Yearly Totals for Each Product Line
st.header("Yearly Totals")

yearly_totals = df.groupby("Product Line").sum().reset_index()
st.write(yearly_totals[[
    "Product Line", "Revenue", "Labor Cost", "COGS", 
    "Marketing", "Gross Profit", "Net Profit"
]])

# Step 7: Display Grand Total for All Product Lines
st.subheader("Grand Total for All Product Lines")
grand_total = yearly_totals[[
    "Revenue", "Labor Cost", "COGS", "Marketing", 
    "Gross Profit", "Net Profit"
]].sum()
st.write(grand_total)
