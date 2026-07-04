import pandas as pd
import matplotlib.pyplot as plt

# Load data
khartoum_sat = pd.read_csv('khartoum_nightlights_2021_2026.csv', parse_dates=['date'])
khartoum_conflict = pd.read_csv('khartoum_conflict_monthly.csv', parse_dates=['year_month'])

fig, ax1 = plt.subplots(figsize=(14, 7))

# left axis: Satellite Radiance
color = '#2ca02c'
ax1.set_xlabel('Timeline', fontsize=12)
ax1.set_ylabel('VIIRS Nightlight Radiance', color=color, fontsize=12)
ax1.plot(khartoum_sat['date'], khartoum_sat['mean_radiance'], color=color, marker='o', linewidth=2, label='Sat Signal')
ax1.tick_params(axis='y', labelcolor=color)

# right axis: ACLED Conflict Events
ax2 = ax1.twinx()
color = "#f50c0c"
ax2.set_ylabel('ACLED Monthly Kinetic Conflict Events', color=color, fontsize=12)
ax2.bar(khartoum_conflict['year_month'], khartoum_conflict['conflict_events'], color=color, alpha=0.4, width=20, label='Kinetic Attacks')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Sensor Fusion Validation: Remote Sensed Radiance vs. Ground Truth Kinetic Conflict (Khartoum)', fontsize=14, fontweight='bold')
fig.tight_layout()
plt.show()