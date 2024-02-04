# Data Cleaning

General strategy:

- Create "truth" masks for training/testing data
- Divide the scenes into training and testing data sets, splitting strata roughly evenly in  terms of day/night.
- Crop each set of Landsat images and masks into many smaller scenes, filtering for only scenes in proximity to the Great Salt Lake. (Be sure to include some land-only smaller scenes. But we don't want Utah Lake included.)

A helpful tutorial on generating raster masks from shape files can be found [here](https://lpsmlgeo.github.io/2019-09-22-binary_mask/).

Thoughts:
LandsatXplore automatically downloads both Systematic Terrain Correction (L1GT) and Terrain Precision Correction (L1TP) scenes, but only L1TP scenes seem to have useable data for this time and region.

Satellite images contain borders of no data. How do we handle this when machine learning? Some quick internet searches reveal that TorchGeo samplers don't have a great way of avoiding null data regions. And our input data will also have no-data borders, so we need some way of robustly handling null data regions.
One option is to make a truth mask where 1 = lake AND data, and 0 = no lake OR no data. Then after applying the model and getting results, a null data mask is applied to the output to signify null regions. This seems more straightforward than trying to avoid the null regions with sampling.

TorchGeo Landsat class assumes a date stamp in .TIF file name. This date stamp is used to define the bounding box in time. Later, TorchGeo will use the bounding box to determine which truth mask corresponds with which scene. Because we have multiple images in the same area on the same day, we need a bounding box that is more precise than one day. get_new_display_id() replaces the date stamp in the file name with a datetime stamp. Without a datetime stamp, the truth mask files cannot be properly assigned to their corresponding scene.