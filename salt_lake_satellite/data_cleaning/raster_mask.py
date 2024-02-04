import rasterio
from rasterio.features import rasterize
import geopandas as gpd

def get_tiff_crs(tiff_path):
    """Given a geo tiff file path, return the crs of the the file"""

    with rasterio.open(tiff_path, 'r') as source:
        crs = source.crs
    return str(crs).lower()

def shape_to_raster(shape, raster_extent, raster_transform):
    """Given a set of polygon shapes, a raster extent, and a raster transform, return a raster image of the shape. A value of 1 in the returned raster denotes inside the polygon, and a value of 0 denotes outside the polygon."""

    shape_geometries = [shapes for shapes in shape.geometry]
    shape_raster = rasterize(shape_geometries,
                       out_shape=raster_extent,
                       transform=raster_transform,
                       all_touched=False)
    return shape_raster

def shapefile_to_maskfile(shape_path, raster_path, output_path):
    """Given a shape file path, a raster file path, and an output path, creates a raster file of the shape with the same resolution and crs as the raster file."""

    raster_crs = get_tiff_crs(raster_path)

    with rasterio.open(raster_path, 'r') as source:
        raster_extent = source.shape
        raster_transform = source.transform
        raster_meta = source.meta
        nodata_mask = source.read_masks(1)

    shape = gpd.read_file(shape_path)
    shape = shape.to_crs(raster_crs)

    shape_raster = shape_to_raster(shape, raster_extent, raster_transform)
    mask_raster = nodata_mask/255 * shape_raster

    mask_raster = mask_raster.astype("uint16")
    mask_meta = raster_meta.copy()
    mask_meta.update({'count': 1})
    with rasterio.open(output_path, 'w', **mask_meta) as dst:
        dst.write(mask_raster * 255, 1)
