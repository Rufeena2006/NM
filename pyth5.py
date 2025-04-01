import pandas as pd
data={
  "Name":["John Doe","Jane Smith","Emily Davis"]
  "Age":[45,50,60]
"Cholesterol":[180,220,190]
}
df=pd.DataFrame(data)
high_risk_patients = df[df["Cholesterol"] > 200]
print(high_risk_patients)
