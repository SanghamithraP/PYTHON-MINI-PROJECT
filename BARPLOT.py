import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample exam results data
data = pd.DataFrame({
    "Department": ["Computer Science", "Math", "Physics", "Biology", "Chemistry"],
    "Average Grade": [85, 78, 82, 74, 80]
})

# Streamlit UI
st.title("Online Exam Results Analyzer")

# Bar Plot: Grade Distribution Across Departments
st.subheader("Grade Distribution by Department")

# Create the bar plot
fig, ax = plt.subplots()
ax.bar(data["Department"], data["Average Grade"], color='skyblue')

# Add labels and title
ax.set_xlabel("Department")
ax.set_ylabel("Average Grade")
ax.set_title("Grade Distribution Across Departments")
ax.set_xticklabels(data["Department"], rotation=45)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot in Streamlit
st.pyplot(fig)