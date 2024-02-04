from torchgeo.datasets import BoundingBox
import geopandas as gpd
from shapely.geometry import Polygon

def bounds_to_roi(bounds, bounds_crs, dataset):
    """Given a list of bounds in lat lon, calculates a TorchGeo bounding box in the dataset's crs"""
    project_polygon = gpd.GeoDataFrame(index=[0], crs=bounds_crs, geometry=[Polygon(bounds)])
    project_polygon = project_polygon.to_crs(dataset.crs)
    [minx, miny, maxx, maxy] = list(project_polygon.geometry.total_bounds)
    mint = dataset.bounds.mint
    maxt = dataset.bounds.maxt
    roi = BoundingBox(minx, maxx, miny, maxy, mint, maxt)
    return roi