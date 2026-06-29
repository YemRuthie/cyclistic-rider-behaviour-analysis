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

# Create day of week
df["day_of_week"] = df["started_at"].dt.day_name()


day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

# Count rides by rider type and day
summary = (
    df.groupby(["member_casual", "day_of_week"])
      .size()
      .reset_index(name="ride_count")
)

summary["day_of_week"] = pd.Categorical(
    summary["day_of_week"],
    categories=day_order,
    ordered=True
)

summary = summary.sort_values(
    by="day_of_week"
) 

print(summary)

# Save results
summary.to_csv(
    "output/06_day_of_week_analysis.csv",
    index=False
)