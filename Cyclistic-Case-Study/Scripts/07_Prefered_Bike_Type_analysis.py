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
    df.groupby(["member_casual", "rideable_type"])
      .size()
      .reset_index(name="ride_count")
)
summary.sort_values(
    by="ride_count",
    ascending=False,
    inplace=True
)

print(summary)

# Save results
summary.to_csv(
    "output/07_Prefered_Bike_Type_analysis.csv",
    index=False
)