import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Profit Calculator", layout="wide")

st.title("💰 Profit Calculator Dashboard")

# --- Create two columns ---
col1, col2 = st.columns(2)

# --- Left column: Expense inputs ---
with col1:
    st.header("🧾 Expenses")
    workers = st.slider("Number of Workers", 1, 200, 10)
    hourly_wage = st.number_input("Hourly Wage (per hour)", value=15.0, step=0.5)
    hours_per_worker = st.number_input("Hours per Worker (period)", value=160, step=1)
    fixed_cost = st.number_input("Fixed Cost (period)", value=5000.0, step=1.0)

# --- Right column: Income inputs ---
with col2:
    st.header("💵 Income")
    orders = st.number_input("Number of Orders (period)", value=1000, step=1)
    AOV = st.number_input("Average Order Value (AOV)", value=12.0, step=0.5)
    
# --- Right column: Income inputs ---
with col3:
    st.header("💵 Trial")
    trial = st.number_input("Number of Orders (period)", value=1000, step=1)

# --- Calculations ---
income = orders * AOV
expenses = (workers * hourly_wage * hours_per_worker) + fixed_cost
profit = income - expenses

# --- Results section ---
st.markdown("---")
st.header("📊 Results")

col3, col4, col5 = st.columns(3)
col3.metric("Net Income", f"${income:,.2f}")
col4.metric("Net Expenses", f"${expenses:,.2f}")
col5.metric("Net Profit", f"${profit:,.2f}")

# --- Simulate a dynamic range for visualization ---
# This creates data points showing how income/expenses vary as orders increase
order_range = list(range(0, int(orders * 1.5), max(1, int(orders / 50))))
income_values = [o * AOV for o in order_range]
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
    yaxis_title="Amount ($)",
    hovermode="x unified",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)
