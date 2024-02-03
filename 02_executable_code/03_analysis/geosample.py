import torch
from torchgeo.datasets import Landsat8, BoundingBox
from torchgeo.samplers import RandomGeoSampler
import yaml
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from shapely.geometry import Polygon
import geopandas as gpd

# Load parameters
config = yaml.safe_load(open('../../project_config.yml'))
landsat_crs = config['landsat']['crs']
landsat_bands = config['landsat']['bands'] # B01-B11
landsat_path = '../../04_processed_data/01_landsat_extracted/'
landsat_summary_file = f"../../{config['landsat']['summary_file']}"
project_bounds_latlon = config['project_bounds']['latlon']
project_bounds_crs = config['project_bounds']['crs']

# Define Landsat 8 & 9 datatype
# FYI: Landsat8 class assumes level 2 surface reflectance products ['SR_B4', 'SR_B3', 'SR_B2']
Landsat8.rgb_bands = ['B4', 'B3', 'B2']
landsat_ds = Landsat8(
    paths=landsat_path,
    crs=landsat_crs,
    bands=landsat_bands
)

# Calculate project bounds
project_polygon = gpd.GeoDataFrame(index=[0], crs=project_bounds_crs, geometry=[Polygon(project_bounds_latlon)])
project_polygon = project_polygon.to_crs(landsat_crs)
[minx, miny, maxx, maxy] = list(project_polygon.geometry.total_bounds)
mint = landsat_ds.bounds.mint
maxt = landsat_ds.bounds.maxt
project_bounds = BoundingBox(minx, maxx, miny, maxy, mint, maxt)

# TorchGeo sampler
sampler = RandomGeoSampler(landsat_ds, size=(512, 512), length=20, roi=project_bounds)

