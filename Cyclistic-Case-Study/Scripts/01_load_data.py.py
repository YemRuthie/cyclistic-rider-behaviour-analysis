import pandas as pd

df = pd.read_csv("data/202605-divvy-tripdata.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst Five Rows:")
print(df.head())