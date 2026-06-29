import pandas as pd

# Load data
df = pd.read_csv("data/202605-divvy-tripdata.csv")

# Convert dates to datetime format
df["started_at"] = pd.to_datetime(df["started_at"])
df["ended_at"] = pd.to_datetime(df["ended_at"])

# Create ride length in minutes
df["ride_length"] = (
    df["ended_at"] - df["started_at"]
).dt.total_seconds() / 60

# Create day of week
df["day_of_week"] = df["started_at"].dt.day_name()

# Create month
df["month"] = df["started_at"].dt.month_name()

# Create hour of day
df["hour"] = df["started_at"].dt.hour

# Check results
print(df[[
    "started_at",
    "ended_at",
    "ride_length",
    "day_of_week",
    "month",
    "hour"
]].head())

# Summary
print("\nRide Length Summary:")
print(df["ride_length"].describe())