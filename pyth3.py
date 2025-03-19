import numpy as np

# Store a week's heart rate readings
heart_rates = np.array([72, 75, 78, 80, 76, 74, 73])

print("Average Heart Rate:", np.mean(heart_rates))
print("Highest Heart Rate:", np.max(heart_rates))
print("Lowest Heart Rate:", np.min(heart_rates))
