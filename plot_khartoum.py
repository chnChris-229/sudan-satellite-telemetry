import pandas as pd
import matplotlib.pyplot as plt

# 1. load data from "Khartoum_nightlights_2021_2026.csv" file saved
try:
    df = pd.read_csv('khartoum_nightlights_2021_2026.csv')
    df['date'] = pd.to_datetime(df['date'])
    print(f"Successfully loaded {len(df)} monthly observations.")
except FileNotFoundError:
    print("Error: Could not find the CSV file. Make sure it's in the same directory.")
    exit()

# 2. plotting canvas
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['mean_radiance'], marker='o', color='#2ca02c', linewidth=2, label='Mean Nightlight Radiance')

# 3. Historical Structural Shock (War Outbreak: April 15, 2023)
war_date = pd.Timestamp('2023-04-15')
plt.axvline(war_date, color='red', linestyle='--', linewidth=1.5, label='War Outbreak (April 2023)')

# 4. add details to chart
plt.title('Khartoum Infrastructure Degradation Proxy (2021 - 2026)', fontsize=14, fontweight='bold')
plt.xlabel('Timeline', fontsize=12)
plt.ylabel('Mean Radiance (nanoWatts/cm²/sr)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')

plt.gcf().autofmt_xdate()

plt.show()