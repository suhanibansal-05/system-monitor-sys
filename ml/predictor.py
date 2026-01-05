import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/metrics.csv")


X = df[["timestamp"]]
y = df["cpu"]

model = LinearRegression()
model.fit(X, y)

future_time = [[df["timestamp"].max() + 60]]
predicted_cpu = model.predict(future_time)

print("Predicted CPU (next minute):", predicted_cpu[0])
