import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set page layout
st.set_page_config(page_title="Online Exam Results Analyzer", layout="centered")

st.title("Online Exam Results Analyzer")

# -----------------------------------
# Section 1: Student Performance Heatmap
# -----------------------------------
st.subheader("1. Student Performance Heatmap")

# Sample data
data1 = pd.DataFrame({
    "Student": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "MCQs": [85, 78, 92, 74, 88],
    "Theory": [80, 75, 89, 70, 85],
    "Practical": [90, 82, 95, 76, 92]
})
data1.set_index("Student", inplace=True)

# Heatmap
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.heatmap(data1, annot=True, cmap="coolwarm", linewidths=0.5, ax=ax1)
st.pyplot(fig1)

# -----------------------------------
# Section 2: Grade Distribution by Department
# -----------------------------------
st.subheader("2. Grade Distribution by Department")

# Sample data
data2 = pd.DataFrame({
    "Department": ["Computer Science", "Math", "Physics", "Biology", "Chemistry"],
    "Average Grade": [85, 78, 82, 74, 80]
})

# Bar Plot
fig2, ax2 = plt.subplots()
ax2.bar(data2["Department"], data2["Average Grade"], color='skyblue')
ax2.set_xlabel("Department")
ax2.set_ylabel("Average Grade")
ax2.set_title("Grade Distribution Across Departments")
ax2.set_xticklabels(data2["Department"], rotation=45)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig2)

# -----------------------------------
# Section 3: Student Performance Trend
# -----------------------------------
st.subheader("3. Student Performance Trend Over Attempts")

# Sample data
data3 = pd.DataFrame({
    "Exam Attempt": [1, 2, 3, 4, 5],
    "Average Score": [60, 72, 65, 80, 77]
})

# Line Plot
fig3, ax3 = plt.subplots()
ax3.plot(data3["Exam Attempt"], data3["Average Score"], marker='o', linestyle='-', color='b', label="Avg Score")
ax3.set_xlabel("Exam Attempt")
ax3.set_ylabel("Average Score")
ax3.set_title("Performance Trend Over Attempts")
ax3.legend()
ax3.grid(True)
st.pyplot(fig3)
