# Cottonwood Canyons Geology

Rachel Morrison - 2024/01/25

This is a an exploratory data analysis of the geology of Big and Little Cottonwood Canyons in the Wasatch Mountain Range outside of Salt Lake City, Utah. This project aims to apply various data analysis and machine learning techniques to high spectral resolution satellite imagery from Landsat 9 to glean mineralogical insight about the canyons. The geology of the Cottonwood Canyons is well studied, so outcomes of machine learning techniques can be validated with existing geologic maps and literature, making this an excellent site for testing and learning new tools.

## Outline

* `01_notes`: Brainstorming of objectives, ideas, and hypotheses
* `02_executable_code`: Where all of the executed code lives
    * `00_exploratoration`: A sandbox for testing different approaches to cleaning, transformation, interpretation, etc.
    * `01_data_collection`: Any code needed for pulling data from APIs
    * `02_data_cleaning`: Any code used in preliminary cleaning and processing of data lives here.
    * `03_analysis`: Code that draws conclusions from a data set including regression, machine learning models, or calculation of various quantities
    * `04_figure_generation`: Code used to generate figures. Lives separate from analysis
* `03_raw_data`: Small (< 50 MB) raw data sets, or links to where large data sets are stored. Raw data is kept separate from processed data to avoid overwriting initial data.
* `04_processed_data`: Cleaned data sets as well as any other processed data. This directory houses all small (< 50 MB) data sets.
* `05_figures`: Output figures are stored here, not with code.
* `06_documents`: Final presentable files and HTML/LaTeX, etc. used to create documentation
* `cc_canyon`: Custom code package for functions called from files in the code directory. Includes code tests.

## Input Data

### Landsat 9 Level 1 Data of Salt Lake Region on 2022-08-29

Downloaded at https://earthexplorer.usgs.gov/

ID: LC09_L1TP_038032_20220829_20230331_02_T1

Landsat Scene Identifier: LC90380322022241LGN01

Collection Category:	T1
Collection Number:	2
WRS Path:	038
WRS Row:	032

Product Map Projection L1:	UTM
UTM Zone:	12
Datum:	WGS84
Ellipsoid:	WGS84
Grid Cell Size Panchromatic:	15.00
Grid Cell Size Reflective:	30.00
Grid Cell Size Thermal:	30.00

### Geologic map of the Salt Lake City

Downloaded at https://doi.org/10.34191/M-190dm

Geologic map of the Salt Lake City 30' x 60' quadrangle, north-central Utah and Uinta County, Wyoming (M-190DM)

Publish Date: 2003

Map Scale: 1:100,000
