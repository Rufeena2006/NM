import pandas as pd

# Creating a patient DataFrame
data = {
    "Name": ["John Doe", "Jane Smith", "Emily Davis"],
    "Age": [45, 50, 60],
    "Cholesterol": [180, 220, 190]
}

df = pd.DataFrame(data)
df["BMI"] = [24.5, 27.8, 30.2]  # Example BMI values
df_sorted = df.sort_values(by="BMI", ascending=False)


def classify_risk(bmi, cholesterol):
    if bmi >= 30 or cholesterol > 200:
        return "High"
    elif bmi >= 25 or cholesterol > 180:
        return "Medium"
    else:
        return "Low"

df["Risk Level"] = df.apply(lambda row: classify_risk(row["BMI"], row["Cholesterol"]), axis=1)

df.to_csv("processed_patient_data.csv", index=False)
print("Data saved as processed_patient_data.csv")
