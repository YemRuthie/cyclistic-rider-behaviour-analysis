import pandas as pd

# Load cleaned dataset
df = pd.read_csv(
    "output/cyclistic_cleaned.csv"
)

# Group by rider type and time of day
summary = (
    df.groupby(
        ["member_casual", "time_of_day"]
    )
    .size()
    .reset_index(name="ride_count")
)

# Sort results
summary = summary.sort_values(
    by=["member_casual", "time_of_day"]
)

# Display results
print(summary)

# Save results
summary.to_csv(
    "output/10_time_of_day_analysis.csv",
    index=False
)