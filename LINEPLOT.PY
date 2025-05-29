import matplotlib.pyplot as plt
import pandas as pd

# Sample exam results data
data = pd.DataFrame({
    "Exam Attempt": [1, 2, 3, 4, 5],
    "Average Score": [60, 72, 65, 80, 77]
})

# Create a line plot
plt.figure(figsize=(8, 5))
plt.plot(data["Exam Attempt"], data["Average Score"], marker='o', linestyle='-', color='b', label="Avg Score")

# Add labels and title
plt.xlabel("Exam Attempt")
plt.ylabel("Average Score")
plt.title("Performance Trend Over Attempts")
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
