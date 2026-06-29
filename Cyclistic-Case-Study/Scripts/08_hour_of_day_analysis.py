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
# Create hour of day
df["hour"] = df["started_at"].dt.hour

summary = (
    df.groupby(["member_casual", "hour"])
      .size()
      .reset_index(name="ride_count")
)

summary = summary.sort_values(
    by=["member_casual", "hour"]
)

print(summary)

summary.to_csv(
    "output/08_hour_of_day_analysis.csv",
    index=False
)