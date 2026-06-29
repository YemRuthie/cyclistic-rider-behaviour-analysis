import pandas as pd

df = pd.read_csv("data/202605-divvy-tripdata.csv")

df["started_at"] = pd.to_datetime(df["started_at"])
df["ended_at"] = pd.to_datetime(df["ended_at"])

df["ride_length"] = (
    df["ended_at"] - df["started_at"]
).dt.total_seconds() / 60

print("Before Cleaning:")
print(df["ride_length"].describe())

# Remove rides shorter than 1 minute
df = df[df["ride_length"] >= 1]

# Remove rides longer than 24 hours
df = df[df["ride_length"] <= 1440]

print("\nAfter Cleaning:")
print(df["ride_length"].describe())

print("\nRemaining Rows:")
print(len(df))