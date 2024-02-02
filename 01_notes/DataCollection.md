# Data Collection

LandSat data can be manually downloaded at [EarthExplore](https://earthexplorer.usgs.gov/) or can be programatically downloaded with the `landsatxplore` package ([Github repo](# FYI: See https://github.com/yannforget/landsatxplore/tree/master for dataset IDs)).

We are using Landsat 8 & 9 Collection 2 Level 1 & 2 data. The `landsatxplore` dataset id is `landsat_ot_c2_l1`.

`landsatxplore` is using an outdated version of `click` which is incompatible with TorchGeo.

Data scenes are not screened during download. Filtering for cloud level, day/night, and snow amount should be evaluated during the modeling stage.