import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
khartoum = pd.read_csv('khartoum_nightlights_2021_2026.csv', parse_dates=['date'])
port_sudan = pd.read_csv('port_sudan_nightlights_2021_2026.csv', parse_dates=['date'])

fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot Khartoum (Left Axis)
color = '#d62728'
ax1.set_xlabel('Timeline', fontsize=12)
ax1.set_ylabel('Khartoum Radiance (nanoWatts/cm²/sr)', color=color, fontsize=12)
ax1.plot(khartoum['date'], khartoum['mean_radiance'], color=color, marker='o', linewidth=2, label='Khartoum (Conflict Zone)')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, linestyle=':', alpha=0.5)

# Instantiate a second axis that shares the same x-axis
ax2 = ax1.twinx()  
color = '#1f77b4'
ax2.set_ylabel('Port Sudan Radiance (nanoWatts/cm²/sr)', color=color, fontsize=12)
ax2.plot(port_sudan['date'], port_sudan['mean_radiance'], color=color, marker='^', linewidth=2, linestyle='--', label='Port Sudan (Safe Haven)')
ax2.tick_params(axis='y', labelcolor=color)

# War Outbreak
plt.axvline(pd.Timestamp('2023-04-15'), color='black', linestyle='-', linewidth=1.5)
plt.text(pd.Timestamp('2023-04-30'), 5, 'War Outbreak', rotation=90, verticalalignment='center', fontweight='bold')

plt.title('The Spatial Inversion of Light: Conflict Capital vs. Safe Haven Hub (2021-2026)', fontsize=14, fontweight='bold')
fig.tight_layout()
plt.show()