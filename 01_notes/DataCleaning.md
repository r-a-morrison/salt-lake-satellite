# Data Cleaning

General strategy:

- Create "truth" masks for training/testing data
- Crop each set of Landsat images and masks into many smaller scenes, filtering for only scenes in proximity to the Great Salt Lake. (Be sure to include some land-only smaller scenes. But we don't want Utah Lake included.)
- Divide the scenes into training and testing data sets, splitting strata roughly evenly in  terms of cloud cover, snow presence, day/night.

A helpful tutorial on generating raster masks from shape files can be found [here](https://lpsmlgeo.github.io/2019-09-22-binary_mask/).