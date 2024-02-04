from torchgeo.datasets import BoundingBox
import geopandas as gpd
from shapely.geometry import Polygon
from torchgeo.datasets import Landsat8, RasterDataset

def bounds_to_roi(bounds, bounds_crs, dataset):
    """Given a list of bounds in lat lon, calculates a TorchGeo bounding box in the dataset's crs"""
    project_polygon = gpd.GeoDataFrame(index=[0], crs=bounds_crs, geometry=[Polygon(bounds)])
    project_polygon = project_polygon.to_crs(dataset.crs)
    [minx, miny, maxx, maxy] = list(project_polygon.geometry.total_bounds)
    mint = dataset.bounds.mint
    maxt = dataset.bounds.maxt
    roi = BoundingBox(minx, maxx, miny, maxy, mint, maxt)
    return roi

class MaskDataset(RasterDataset):
    filename_regex = r"""
        ^L
        (?P<sensor>[COTEM])
        (?P<satellite>\d{2})
        _(?P<processing_correction_level>[A-Z0-9]{4})
        _(?P<wrs_path>\d{3})
        (?P<wrs_row>\d{3})
        _(?P<date>\d{14})
        _(?P<processing_date>\d{8})
        _(?P<collection_number>\d{2})
        _(?P<collection_category>[A-Z0-9]{2})
        _TRUTH
        \.
    """
    date_format = "%Y%m%d%H%M%S" # Change filenames to match
    is_image = False
    separate_files = False

class Landsat8Dataset(Landsat8):
    filename_regex = r"""
        ^L
        (?P<sensor>[COTEM])
        (?P<satellite>\d{2})
        _(?P<processing_correction_level>[A-Z0-9]{4})
        _(?P<wrs_path>\d{3})
        (?P<wrs_row>\d{3})
        _(?P<date>\d{14})
        _(?P<processing_date>\d{8})
        _(?P<collection_number>\d{2})
        _(?P<collection_category>[A-Z0-9]{2})
        _(?P<band>[A-Z0-9_]+)
        \.
    """
    date_format = "%Y%m%d%H%M%S" # Change filenames to match
    is_image = True
    separate_files = True