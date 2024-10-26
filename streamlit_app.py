import streamlit as st
import pandas as pd

st.title("Profit & Loss Model with Manufacturing Tracker")

# Profit & Loss Section
st.header("Profit & Loss Model")
st.subheader("Enter Product Line Data")

# Input fields for Product Line 1
st.write("### Product Line 1")
sales_p1 = st.number_input("Sales (Product Line 1)", min_value=0.0, value=0.0)
labor_p1 = st.number_input("Labor Costs (Product Line 1)", min_value=0.0, value=0.0)
cogs_p1 = st.number_input("COGS (Product Line 1)", min_value=0.0, value=0.0)
marketing_p1 = st.number_input("Marketing Costs (Product Line 1)", min_value=0.0, value=0.0)
gross_profit_p1 = sales_p1 - labor_p1 - cogs_p1 - marketing_p1

# Input fields for Product Line 2
st.write("### Product Line 2")
sales_p2 = st.number_input("Sales (Product Line 2)", min_value=0.0, value=0.0)
labor_p2 = st.number_input("Labor Costs (Product Line 2)", min_value=0.0, value=0.0)
cogs_p2 = st.number_input("COGS (Product Line 2)", min_value=0.0, value=0.0)
marketing_p2 = st.number_input("Marketing Costs (Product Line 2)", min_value=0.0, value=0.0)
gross_profit_p2 = sales_p2 - labor_p2 - cogs_p2 - marketing_p2

# Display Results
total_revenue = sales_p1 + sales_p2
total_cogs = cogs_p1 + cogs_p2
total_labor = labor_p1 + labor_p2
total_marketing = marketing_p1 + marketing_p2
total_gross_profit = gross_profit_p1 + gross_profit_p2

st.write("### P&L Summary")
st.write(f"Total Revenue: ${total_revenue}")
st.write(f"Total COGS: ${total_cogs}")
st.write(f"Total Labor Costs: ${total_labor}")
st.write(f"Total Marketing Costs: ${total_marketing}")
st.write(f"Total Gross Profit: ${total_gross_profit}")

# Manufacturing Time Tracker Section
st.header("Manufacturing Time Tracker")

# Input fields for Manufacturing Time
st.subheader("Product Line 1")
machining_p1 = st.number_input("Machining (min/unit)", min_value=0.0, value=0.0)
tumbling_p1 = st.number_input("Tumbling (min/unit)", min_value=0.0, value=0.0)
grinding_p1 = st.number_input("Grinding (min/unit)", min_value=0.0, value=0.0)
assembly_p1 = st.number_input("Assembly (min/unit)", min_value=0.0, value=0.0)
laser_p1 = st.number_input("Laser (min/unit)", min_value=0.0, value=0.0)
units_p1 = st.number_input("Units per Month (Product Line 1)", min_value=0, value=0)

# Total time per process for Product Line 1
total_time_p1 = (machining_p1 + tumbling_p1 + grinding_p1 + assembly_p1 + laser_p1) * units_p1
st.write(f"Total Manufacturing Time for Product Line 1: {total_time_p1} minutes")

# Input fields for Product Line 2
st.subheader("Product Line 2")
machining_p2 = st.number_input("Machining (min/unit)", min_value=0.0, value=0.0)
tumbling_p2 = st.number_input("Tumbling (min/unit)", min_value=0.0, value=0.0)
grinding_p2 = st.number_input("Grinding (min/unit)", min_value=0.0, value=0.0)
assembly_p2 = st.number_input("Assembly (min/unit)", min_value=0.0, value=0.0)
laser_p2 = st.number_input("Laser (min/unit)", min_value=0.0, value=0.0)
units_p2 = st.number_input("Units per Month (Product Line 2)", min_value=0, value=0)

# Total time per process for Product Line 2
total_time_p2 = (machining_p2 + tumbling_p2 + grinding_p2 + assembly_p2 + laser_p2) * units_p2
st.write(f"Total Manufacturing Time for Product Line 2: {total_time_p2} minutes")

# Grand Total Time
grand_total_time = total_time_p1 + total_time_p2
st.write(f"### Grand Total Manufacturing Time: {grand_total_time} minutes")
