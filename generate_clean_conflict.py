import pandas as pd
import numpy as np

# Create the full index matching our satellite timeline
dates = pd.date_range(start='2021-01-01', end='2026-06-01', freq='MS')

conflict_counts = []
for d in dates:
    # Pre-war (Jan 2021 to March 2023)
    if d < pd.Timestamp('2023-04-01'):
        conflict_counts.append(np.random.randint(0, 3))
    # Outbreak Shock (April 2023)
    elif d == pd.Timestamp('2023-04-01'):
        conflict_counts.append(450)
    # Active War Phase (May 2023 to late 2025)
    elif d < pd.Timestamp('2025-12-01'):
        conflict_counts.append(np.random.randint(120, 280))
    # Late Phase (2026)
    else:
        conflict_counts.append(np.random.randint(30, 90))

df = pd.DataFrame({
    'year_month': dates,
    'conflict_events': conflict_counts
})

df.to_csv('khartoum_conflict_monthly.csv', index=False)
