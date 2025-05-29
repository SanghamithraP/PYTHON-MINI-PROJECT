import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample exam results data
data = pd.DataFrame({
    "Student": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "MCQs": [85, 78, 92, 74, 88],
    "Theory": [80, 75, 89, 70, 85],
    "Practical": [90, 82, 95, 76, 92]
})

# Set Student as index for heatmap structure
data.set_index("Student", inplace=True)

# Create heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(data, annot=True, cmap="coolwarm", linewidths=0.5)

# Add title
plt.title("Exam Results Heatmap")

# Display the plot
plt.show()
