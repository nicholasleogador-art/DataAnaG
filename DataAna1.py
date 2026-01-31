import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="My First Streamlit App", page_icon="🚀")

# 2. Header and Title
st.title("Thamer OTS! 👋")
st.write("This is a simple app to get you started.")

# 3. Sidebar for Inputs
st.sidebar.header("User Settings")
name = st.sidebar.text_input("Enter your name", placeholder="Type here...")

# 4. Interactive Elements
if name:
    st.success(f"Welcome to the app, {name}!")

# 5. Data Visualization Example
st.subheader("Random Data Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Category A', 'Category B', 'Category C']
)

st.line_chart(chart_data)

# 6. Checkbox to show raw data
if st.checkbox("Show raw data"):
    st.write(chart_data)