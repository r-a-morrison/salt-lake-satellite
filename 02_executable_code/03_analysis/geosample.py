from torchgeo.datasets import Landsat8, BoundingBox
from torchgeo.samplers import RandomGeoSampler
import yaml
import pandas as pd
from shapely.geometry import Polygon
import geopandas as gpd
from salt_lake_satellite.analysis import geosample

# Load parameters
config = yaml.safe_load(open('project_config.yml'))
landsat_crs = config['landsat']['crs']
landsat_bands = config['landsat']['bands'] # B01-B11
landsat_train_path = '04_processed_data/02_landsat_train/'
project_bounds_latlon = config['project_bounds']['latlon']
project_bounds_crs = config['project_bounds']['crs']

train_df = pd.read_csv(config['train_summary'])
train_paths = [f"{landsat_train_path}{display_id}/" for display_id in train_df['display_id']]

landsat_ds = Landsat8(
    paths=train_paths,
    crs=landsat_crs,
    bands=landsat_bands
)

# Calculate project bounds
project_bounds = geosample.bounds_to_roi(project_bounds_latlon, project_bounds_crs, landsat_ds)

# TorchGeo sampler
sampler = RandomGeoSampler(landsat_ds, size=(512, 512), length=300, roi=project_bounds)

