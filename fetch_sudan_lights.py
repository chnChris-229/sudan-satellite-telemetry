import ee
import pandas as pd

# initialize google earth api
try:
    ee.Initialize(project='neon-effect-500913-u3')
    print("Google Earth Engine initialized successfully.")
except Exception as e:
    print("Initialization failed. Did you run 'earthengine authenticate'?")
    raise e

# 2. define areas of interest: Khartoum, Sudan
khartoum_bbox = ee.Geometry.Rectangle([32.40, 15.45, 32.65, 15.68])

# 3. VIIRS Nighttime Lights Monthly Dataset
viirs_collection = (ee.ImageCollection('NOAA/VIIRS/DNB/MONTHLY_V1/VCMCFG')
                    .filterDate('2021-01-01', '2026-06-01')
                    .filterBounds(khartoum_bbox)
                    .select('avg_rad'))

# 4. here we want to calculate average light value per month
def calculate_mean_light(image):
    mean_dict = image.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=khartoum_bbox,
        scale=500,
        maxPixels=1e9
    )
    date = ee.Date(image.get('system:time_start')).format('YYYY-MM-dd')
    return ee.Feature(None, {
        'date': date,
        'mean_radiance': mean_dict.get('avg_rad')
    })

print("Extracting data from Google Earth Engine... This takes a few seconds.")
processed_features = viirs_collection.map(calculate_mean_light).getInfo()

# 5. breakdown the GEE response into a Pandas DataFrame
data_list = []
for feature in processed_features['features']:
    props = feature['properties']
    data_list.append({
        'date': props['date'],
        'mean_radiance': props['mean_radiance']
    })

df = pd.DataFrame(data_list)
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date').dropna()

# 6. save raw time series dataset 
df.to_csv('khartoum_nightlights_2021_2026.csv', index=False)
print("Data pipeline completed! File saved as khartoum_nightlights_2021_2026.csv")
print(df.head())