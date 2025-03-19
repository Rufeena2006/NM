# Function to determine BMI category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

patient_bmi = 24.5  # Example BMI value
print("BMI Category:", bmi_category(patient_bmi))
