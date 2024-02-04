from pathlib import Path
import yaml
import rasterio
from rasterio.features import rasterize
import pandas as pd
import geopandas as gpd
from salt_lake_satellite.data_cleaning import raster_mask

# Annotation defined as 1: Lake AND data, or 0: No lake OR no data

# Import parameters
config = yaml.safe_load(open('project_config.yml'))
water_level_shapefile = config['water_level']['shapefile']
landsat_dir = '04_processed_data/01_landsat_extracted/'
train_dir = '04_processed_data/04_raster_mask_train/'
test_dir = '04_processed_data/05_raster_mask_test/'

train_df = pd.read_csv(config['train']['summary_file'])
test_df = pd.read_csv(config['test']['summary_file'])

for scene in train_df['display_id']:
    raster_path = f'{landsat_dir}{scene}/{scene}_B10.TIF'
    output_path = f'{train_dir}{scene}_TRUTH.TIF'
    Path(train_dir).mkdir(parents=True, exist_ok=True)
    raster_mask.shapefile_to_maskfile(water_level_shapefile, raster_path, output_path)

for scene in test_df['display_id']:
    raster_path = f'{landsat_dir}{scene}/{scene}_B10.TIF'
    output_path = f'{test_dir}{scene}_TRUTH.TIF'
    Path(test_dir).mkdir(parents=True, exist_ok=True)
    raster_mask.shapefile_to_maskfile(water_level_shapefile, raster_path, output_path)