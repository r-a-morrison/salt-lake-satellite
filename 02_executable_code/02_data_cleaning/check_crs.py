import pandas as pd
import rasterio
import geopandas as gpd

landsat_summary_file = '03_raw_data/Landsat/lansat_summary_2024-01-28.csv'
landsat_dir = '04_processed_data/01_landsat_extracted/'
gsl_water_level_2016_file = '03_raw_data/Utah_Great_Salt_Lake_Water_Level_2016/GSLWaterLevel2016.shp'

scenes_df = pd.read_csv(landsat_summary_file)

scene_id = scenes_df['display_id'][0]
raster_path = f'{landsat_dir}{scene_id}/{scene_id}_B1.TIF'
with rasterio.open(raster_path, 'r') as src:
    raster_meta = src.meta
print(f'Landsat CRS: {raster_meta["crs"]}')

gsl_water_level_2016_shp = gpd.read_file(gsl_water_level_2016_file)
print(f'Water Level Shape File: {gsl_water_level_2016_shp.crs}')


