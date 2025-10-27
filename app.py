import streamlit as st

st.title("Profit Calculator")

workers = st.slider("Number of Workers", 1, 200, 10)
hourly_wage = st.number_input("Hourly Wage (per hour)", value=20.0, step=0.5)
hours_per_worker = st.number_input("Hours per Worker (period)", value=160, step=1)
fixed_cost = st.number_input("Fixed Cost (period)", value=5000.0, step=1.0)
orders = st.number_input("Number of Orders (period)", value=1000, step=1)
AOV = st.number_input("Average Order Value (AOV)", value=50.0, step=0.5)

# Calculations
income = orders * AOV
expenses = (workers * hourly_wage * hours_per_worker) + fixed_cost
profit = income - expenses

# Display metrics
st.metric("Net Income", f"${income:,.2f}")
st.metric("Net Expenses", f"${expenses:,.2f}")
st.metric("Net Profit", f"${profit:,.2f}")

# Chart
st.bar_chart({
    "Net Income": [income],
    "Net Expenses": [expenses],
    "Net Profit": [profit]
})
