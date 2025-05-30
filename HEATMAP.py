import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample exam results data
data = pd.DataFrame({
    "Student": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "MCQs": [85, 78, 92, 74, 88],
    "Theory": [80, 75, 89, 70, 85],
    "Practical": [90, 82, 95, 76, 92]
})

# Set Student as index for heatmap structure
data.set_index("Student", inplace=True)

# Streamlit UI
st.title("Online Exam Results Analyzer")
st.subheader("Performance Heatmap")

# Create heatmap
fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(data, annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)

# Display the heatmap in Streamlit
st.pyplot(fig)