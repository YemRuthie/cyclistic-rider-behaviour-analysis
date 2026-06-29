import pandas as pd

# Load data
df = pd.read_csv("data/202605-divvy-tripdata.csv")

# Convert dates
df["started_at"] = pd.to_datetime(df["started_at"])
df["ended_at"] = pd.to_datetime(df["ended_at"])

# Create ride length
df["ride_length"] = (
    df["ended_at"] - df["started_at"]
).dt.total_seconds() / 60

# Clean data
df = df[df["ride_length"] >= 1]
df = df[df["ride_length"] <= 1440]

# Compare members and casual riders
summary = (
    df.groupby("member_casual")["ride_length"]
      .agg(["count", "mean", "median", "min", "max"])
)

print(summary)
summary.to_csv(
    "output/05_member_vs_casual_duration.csv")