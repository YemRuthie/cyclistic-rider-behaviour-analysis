import pandas as pd

df = pd.read_csv("data/202605-divvy-tripdata.csv")

print("Dataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nMember Types:")
print(df["member_casual"].value_counts())