import pandas as pd

# Creating a patient DataFrame
data = {
    "Name": ["John Doe", "Jane Smith", "Emily Davis"],
    "Age": [45, 50, 60],
    "Cholesterol": [180, 220, 190]
}

df = pd.DataFrame(data)
print(df)
