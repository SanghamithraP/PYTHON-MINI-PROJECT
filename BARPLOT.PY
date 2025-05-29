import matplotlib.pyplot as plt
import pandas as pd

# Sample exam results data
data = pd.DataFrame({
    "Department": ["Botany", "Math", "Physics", "Zoology","Chemistry"],
    "Average Grade": [85, 78, 82, 74, 80]
})

# Create a bar plot
plt.figure(figsize=(8, 5))
plt.bar(data["Department"], data["Average Grade"], color='skyblue')

# Add labels and title
plt.xlabel("Department")
plt.ylabel("Average Grade")
plt.title("Grade Distribution by Department")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()
