import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon
from salt_lake_satellite.data_collection import earth_explorer
from datetime import date
import yaml

config = yaml.safe_load(open('project_config.yml'))

# Import parameters for Landsat data
project_bounds_latlon = config['project_bounds_latlon']
landsat_crs = config['landsat']['crs']
start_date = config['annotate_start_date']
end_data = config['annotate_end_date']
landsat_dataset = config['landsat']['dataset']
output_dir = '03_raw_data/Landsat/'

# Transform crs of project bounds
project_polygon = gpd.GeoDataFrame(index=[0], crs=landsat_crs, geometry=[project_bounds_latlon])
project_bounds = list(project_polygon.geometry.total_bounds)

# Search for Landsat data taken in same months as 2016 LiDAR study
api = earth_explorer.initialize_usgs_api()
scenes = api.search(
    dataset=landsat_dataset,
    bbox=project_bounds,
    start_date=start_date,
    end_date=end_data
)
api.logout()

# Display basic search results information
scenes_df = earth_explorer.get_search_info(scenes)
scenes_df.to_csv(f'{output_dir}/lansat_summary_{date.today()}.csv', index=False)

# Download results
earth_explorer.download_data(display_ids=scenes_df['display_id'], path_dir=output_dir)





