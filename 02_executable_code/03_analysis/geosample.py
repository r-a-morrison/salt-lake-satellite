from torchgeo.samplers import RandomGeoSampler
import yaml
from salt_lake_satellite.analysis import geosample

# Load parameters
config = yaml.safe_load(open('project_config.yml'))
landsat_crs = config['landsat']['crs']
landsat_bands = config['landsat']['bands'] # B01-B11
landsat_train_path = '04_processed_data/02_landsat_train/'
mask_train_path = '../../04_processed_data/04_raster_mask_train/'
project_bounds_latlon = config['project_bounds']['latlon']
project_bounds_crs = config['project_bounds']['crs']

landsat_ds = geosample.Landsat8Dataset(
    paths=landsat_train_path,
    crs=landsat_crs,
    bands=landsat_bands
)
mask_ds = geosample.MaskDataset(paths=mask_train_path, crs=landsat_crs)

# Calculate project bounds
project_bounds = geosample.bounds_to_roi(project_bounds_latlon, project_bounds_crs, landsat_ds)

# TorchGeo sampler
sampler = RandomGeoSampler(landsat_ds, size=(512, 512), length=300, roi=project_bounds)

train_ds = landsat_ds & mask_ds

