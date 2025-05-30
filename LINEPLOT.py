import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load sample exam results data
data = pd.DataFrame({
    "Exam Attempt": [1, 2, 3, 4, 5],
    "Average Score": [60, 72, 65, 80, 77]
})

# Streamlit UI
st.title("Online Exam Results Analyzer")

# Line Plot: Exam Performance Over Attempts
st.subheader("Student Performance Trend")

# Create the line plot
fig, ax = plt.subplots()
ax.plot(data["Exam Attempt"], data["Average Score"], marker='o', linestyle='-', color='b', label="Avg Score")

# Add labels and title
ax.set_xlabel("Exam Attempt")
ax.set_ylabel("Average Score")
ax.set_title("Performance Trend Over Attempts")
ax.legend()
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)