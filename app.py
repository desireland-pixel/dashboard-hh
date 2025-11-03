import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Profit Calculator", layout="wide")

st.title("💰 Profit Calculator Dashboard (Monthly)")

# --- Create two columns ---
col1, col2, col3 = st.columns(3)

# --- Left column: Expense inputs ---
with col1:
    st.header("🧾 Expenses")
    workers = st.slider("Number of Partners", 1, 200, 30, width=400)
    hourly_wage = st.number_input("Hourly Wage", value=15.0, step=0.5, width=200)
    hours_per_worker = st.number_input("Hours per Partner (monthly)", value=160, step=1, width=200)
    fixed_cost = st.number_input("Fixed Cost", value=5000.0, step=100.0, width=200)

# --- Middle column: Income inputs ---
with col2:
    st.header("💸 Income")
    orders = st.number_input("Number of Orders (monthly)", value=30000, step=50, width=200)
    AOV = st.number_input("Average Order Value (AOV)", value=12.0, step=0.5, width=200)
    commission = st.number_input("Commission (in %)", value=25.0, step=1.0, max_value=40.0, width=200)

# --- Calculations ---
income = orders * AOV * commission * 0.01
expenses = (workers * hourly_wage * hours_per_worker) + fixed_cost
profit = income - expenses

# --- Right column: Income inputs ---
with col3:
    st.header("💵 Results")
    st.metric("Net Income", f"€ {income:,.2f}")
    st.metric("Net Expenses", f"€ {expenses:,.2f}")
    st.metric("Net Profit", f"€ {profit:,.2f}")

# --- Simulate a dynamic range for visualization ---
# This creates data points showing how income/expenses vary as orders increase
order_range = list(range(0, int(orders * 1.5), max(1, int(orders / 50))))
income_values = [(o * AOV * commission * 0.01) for o in order_range]
expense_values = [(workers * hourly_wage * hours_per_worker) + fixed_cost for _ in order_range]

# --- Plotly interactive line chart ---
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=order_range, y=income_values,
    mode='lines', name='Net Income',
    line=dict(width=3)
))

fig.add_trace(go.Scatter(
    x=order_range, y=expense_values,
    mode='lines', name='Net Expenses',
    line=dict(width=3)
))

# Add a vertical marker at the current "orders" input
fig.add_vline(
    x=orders, line_dash="dash", line_color="gray",
    annotation_text=f"Current Orders: {orders}", annotation_position="top right"
)

fig.update_layout(
    title="Income vs Expenses Over Order Volume",
    xaxis_title="Number of Orders",
    yaxis_title="Amount (€)",
    hovermode="x unified",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)
