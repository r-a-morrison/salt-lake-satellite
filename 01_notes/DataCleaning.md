# Data Cleaning

General strategy:

- Create "truth" masks for training/testing data
- Divide the scenes into training and testing data sets, splitting strata roughly evenly in  terms of day/night.
- Crop each set of Landsat images and masks into many smaller scenes, filtering for only scenes in proximity to the Great Salt Lake. (Be sure to include some land-only smaller scenes. But we don't want Utah Lake included.)

A helpful tutorial on generating raster masks from shape files can be found [here](https://lpsmlgeo.github.io/2019-09-22-binary_mask/).

Thoughts:
Satellite images contain borders of no data. How do we handle this when machine learning? Some quick internet searches reveal that TorchGeo samplers don't have a great way of avoiding null data regions. And our input data will also have no-data borders, so we need some way of robustly handling null data regions.
One option is to make a truth mask where 1 = lake AND data, and 0 = no lake OR no data. Then after applying the model and getting results, a null data mask is applied to the output to signify null regions. This seems more straightforward than trying to avoid the null regions with sampling.