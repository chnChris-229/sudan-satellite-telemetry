import ee
import pandas as pd

# 1. initialize GEE
try:
    ee.Initialize(project='neon-effect-500913-u3')
    print("Google Earth Engine initialized successfully.")
except Exception as e:
    print("Initialization failed.")
    raise e

# 2. target bounding boxes 
hubs = {
    'port_sudan': ee.Geometry.Rectangle([37.15, 19.55, 37.28, 19.65]),
    'adre_border': ee.Geometry.Rectangle([22.15, 13.42, 22.25, 13.50])
}

# 3. load VIIRS Dataset
viirs_collection = (ee.ImageCollection('NOAA/VIIRS/DNB/MONTHLY_V1/VCMCFG')
                    .filterDate('2021-01-01', '2026-06-01'))

# 4. Processing Loop for each region
for name, bbox in hubs.items():
    print(f"Extracting time-series arrays for: {name}...")
    
    region_collection = viirs_collection.filterBounds(bbox).select('avg_rad')
    
    def calculate_mean_light(image):
        mean_dict = image.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=bbox,
            scale=500,
            maxPixels=1e9
        )
        date = ee.Date(image.get('system:time_start')).format('YYYY-MM-dd')
        return ee.Feature(None, {
            'date': date,
            'mean_radiance': mean_dict.get('avg_rad')
        })
        
    processed_features = region_collection.map(calculate_mean_light).getInfo()
    
    # breakdown into DataFrame
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
    
    # save target file
    filename = f'{name}_nightlights_2021_2026.csv'
    df.to_csv(filename, index=False)
    print(f"Saved {filename}")

print("\nAll comparative data ingestion completed successfully!")