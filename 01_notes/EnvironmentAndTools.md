# Environment and Tools

For this project I chose to use Poetry for package management. It does not play nicely with GDAL, but we'll be using geopandas and rasterio instead. Anaconda can also be nice, but it installs a plethora of packages and tools system-wide, and I prefer to keep my system tidy.

## Environment setup

Create: `poetry init`  (or `poetry install` if poetry.lock is present)

Activate: `poetry shell`

Deactivate:  `deactivate`

Save to lockfile: `poetry lock`

Install package: `poetry add my_package` 

Remove: `poetry remove my_package`

Update: Change `pyproject.toml` and run `poetry update` 

## Project Structure

It's convenient to have multiple python files have access to general utility functions and test functions. I find [this](https://xebia.com/blog/a-practical-guide-to-setuptools-and-pyproject-toml/) reference helpful.

I use a `setup.cfg` file at the root level and __in an environment__ run `pip3 install -e .` to install the project modules as a package. `__init__.py` lets code import functions without having to type the entire path.

For testing, I've included a data folder and  a `context.py` file to give tests access to the data.

## Geospatial Tools

GDAL is powerful and complex. It's often used from the command line, but Python GDAL is available. Rasterio is a more "Pythonic" library that uses GDAL. It is often used in conjunction with geopandas. It has inherent incompatibilities with Python GDAL, so only one should be chosen. Earthpy is a package using rasterio and geopandas with plotting functionality. Rioxarray is a package using rasterio and xarray that provides multi-spectral functionality. Here I use a rasterio/geopandas/Earthpy/rioxarray ecosystem. TorchGeo is my tool of choice for geospatial machine learning with multi-spectral satellite data.

Caution! `landsatxplore` and `TorchGeo` currently require incompatible versions of `click`. I first pip installed `landsatxplore`, then later removed it and then installed `TorchGeo`. These tools should probably be broken up into separate projects in the future until this is fixed.