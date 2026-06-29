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

df["ride_length"] = df["ride_length"].round(2)

# Clean data
df = df[df["ride_length"] >= 1]
df = df[df["ride_length"] <= 1440]

# Create day of week
df["day_of_week"] = df["started_at"].dt.day_name()

# Create hour of day
df["hour"] = df["started_at"].dt.hour

# Create time of day
def get_time_of_day(hour):

    if 5 <= hour <= 11:
        return "Morning"

    elif 12 <= hour <= 16:
        return "Afternoon"

    elif 17 <= hour <= 21:
        return "Evening"

    else:
        return "Night"


df["time_of_day"] = df["hour"].apply(
    get_time_of_day
)

# Create month
df["month"] = df["started_at"].dt.month_name()

# Save master dataset
df.to_csv(
    "output/cyclistic_cleaned.csv",
    index=False
)

print("Master dataset created successfully.")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

print("\nColumns:")
print(df.columns.tolist())