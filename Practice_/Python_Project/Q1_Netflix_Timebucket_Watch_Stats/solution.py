# Data Available in this Dataframe:
df = data.copy()

# Convert timestamp to datetime
df['ts'] = pd.to_datetime(df['ts'])

# Filter for October 21, 2025
df = df[df['ts'].dt.date == pd.to_datetime('2025-10-21').date()]

# Extract hour
df['hour'] = df['ts'].dt.hour

# Aggregate seconds per hour and get top 5
result = (
    df.groupby('hour', as_index=False)['seconds']
      .sum()
      .sort_values('seconds', ascending=False)
      .head(5)
)

# return the Dataframe
result
