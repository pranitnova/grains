import streamlit as st
import pandas as pd

# Set up the layout
st.title("Silver Grains")
st.sidebar.header("Inputs")
# Accept float input for quantity
quantity = st.sidebar.number_input(
    "Quantity (in tons)", value=1.0, min_value=0.02, step=0.02, format="%.02f"
)
serial_start = st.sidebar.number_input("Serial Start Number", value=1, min_value=1)
batch_start = st.sidebar.number_input("Batch Start Number", value=100, min_value=0)

# Calculate table data
data = []
serial_end = serial_start
batch_end = batch_start

# Assuming each ton or part thereof increments serial by 50 and batch by 50
for _ in range(int(quantity)):
    serial_end = serial_start + 49  # Increment for whole ton
    batch_end = batch_start + 49
    row = [1, serial_start, serial_end, batch_start, batch_end]
    data.append(row)
    serial_start = serial_end + 1
    batch_start = batch_end + 1

# Handling decimal part of quantity if exists
decimal_part = quantity - int(quantity)
if decimal_part > 0:
    serial_end = serial_start + int(49 * decimal_part)  # Adjusted for decimal quantity
    batch_end = batch_start + int(49 * decimal_part)  # Adjusted for decimal quantity
    row = [decimal_part, serial_start, serial_end, batch_start, batch_end]
    data.append(row)

# Create DataFrame
df = pd.DataFrame(
    data,
    columns=[
        "Quantity (Tons)",
        "Serial Start",
        "Serial End",
        "Batch Start",
        "Batch End",
    ],
)

# Display the table
st.table(df.assign(hack="").set_index("hack"))
