import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon
from salt_lake.utils.data_collection import earth_explorer
from datetime import date

# Define parameters for Landsat data
project_bound_latlon = Polygon([[-113.42559815,41.67906622],
                                [-112.69091427,40.50542039],
                                [-111.84082032,40.80965167],
                                [-112.5755042,41.97789442],
                                [-113.42559815,41.67906622]])
crs = 'epsg:4326'
start_date = '2016-09-01'
end_data = '2016-11-31'
# FYI: See https://github.com/yannforget/landsatxplore/tree/master for dataset IDs
landsat_dataset='landsat_ot_c2_l1' # Landsat 8 & 9 Collection 2 Level 1 & 2
output_dir = '../../03_raw_data/Landsat/'

# Transform crs of project bounds
project_polygon = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[project_bound_latlon])
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
scenes_df.to_csv(f'{output_dir}/lansat_summary_{date.today()}.csv')

# Download results
earth_explorer.download_data(display_ids=scenes_df['display_id'], path_dir=output_dir)





