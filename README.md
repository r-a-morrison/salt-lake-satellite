# Great Salt Lake Satellite Data Exploration

NOTE: Project in Progress

Rachel Morrison - 2024/01/25

This is a an exploratory data analysis of the historical water fill of the Great Salt Lake, Utah. This project aims to apply various data analysis and machine learning techniques to high spectral resolution satellite imagery from Landsat 8 & 9 to glean insight about the historical water levels of the lake. Shapefiles from LiDAR in 2016 are used as labels for training and testing of the data.

## Outline

* `01_notes`: Brainstorming of objectives, ideas, and hypotheses
* `02_executable_code`: Where all of the executed code lives
    * `00_exploration`: A sandbox for testing different approaches to cleaning, transformation, interpretation, etc.
    * `01_data_collection`: Any code needed for pulling data from APIs
    * `02_data_cleaning`: Any code used in preliminary cleaning and processing of data lives here.
    * `03_analysis`: Code that draws conclusions from a data set including regression, machine learning models, or calculation of various quantities
    * `04_figure_generation`: Code used to generate figures. Lives separate from analysis
* `03_raw_data`: (Excluded from git.) Raw data sets, or links to where large data sets are stored. Raw data is kept separate from processed data to avoid overwriting initial data.
* `04_processed_data`: (Excluded from git.) Cleaned data sets as well as any other processed data. This directory houses all small (< 50 MB) data sets.
* `05_figures`: Output figures are stored here, not with code.
* `06_documents`: Final presentable files and HTML/LaTeX, etc. used to create documentation
* `salt_lake_satellite`: Custom code package for functions called from files in the code directory. Includes code tests.

## Input Data

### Landsat 8 & 9 Level 1 Data of Salt Lake Region

Downloaded at https://earthexplorer.usgs.gov/

Collection Category:	T1 & T2

Collection: 2

Product Map Projection L1:	UTM
Datum:	WGS84
Ellipsoid:	WGS84

EPSG:32612
WGS 84 / UTM zone 12N

Grid Cell Size Panchromatic:	15.00
Grid Cell Size Reflective:	30.00
Grid Cell Size Thermal:	30.00

### Shapefiles from 2016 LiDAR Study

https://deploy-preview-2028--gis-utah-gov.netlify.app/data/elevation-and-terrain/2016-lidar-gsl/

https://opendata.gis.utah.gov/datasets/utah::utah-great-salt-lake-water-level-2016/about

Collection Start: 9/3/2016 
Collection End: 11/18/2016
