import pandas as pd
import rasterio
import geopandas as gpd
import yaml

config = yaml.safe_load(open('project_config.yml'))

landsat_dir = '04_processed_data/01_landsat_extracted/'
landsat_summary_file = config['landsat']['summary_file']
landsat_expected_crs = config['landsat']['crs']
gsl_water_level_2016_file = config['water_level']['shapefile']
gsl_water_level_2016_expected_crs = config['water_level']['crs']

scenes_df = pd.read_csv(landsat_summary_file)

scene_id = scenes_df['display_id'][0]
raster_path = f'{landsat_dir}{scene_id}/{scene_id}_B1.TIF'
with rasterio.open(raster_path, 'r') as src:
    raster_meta = src.meta
print(f'Landsat CRS: {raster_meta["crs"]}')
print(f'Landsat Expected CRS: {landsat_expected_crs}')

gsl_water_level_2016_shp = gpd.read_file(gsl_water_level_2016_file)
print(f'Water Level Shape File: {gsl_water_level_2016_shp.crs}')
print(f'Water Level Expected CRS: {gsl_water_level_2016_expected_crs}')


