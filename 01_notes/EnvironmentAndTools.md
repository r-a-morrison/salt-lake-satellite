# Environment and Tools

For this project I chose to use Python a virtual environment with Miniconda for package management. I am fond of Poetry for package management, but it does not play nicely with GDAL. Anaconda can also be nice, but it installs a plethora of packages and tools system-wide, and I prefer to keep my system tidy.

[Miniconda installation](https://docs.conda.io/projects/miniconda/en/latest/): The command line installation is fast and easy.

I found a helpful article on installing GDAL in a virtual environment [here](https://medium.com/@spatsel.cci/using-gdal-with-python-pip-and-windows-10-618d773d8926).

## Environment config files

Both of these go in the project root directory.

`environment.yml` template:

```
name: my_env
channels:
 - conda-forge
dependencies:
 - python=3.11
 - pip
 - pip:
   - -r requirements.txt
```

`requirements.txt` template:

```
pandas==2.2.0
numpy==1.26.0
```

## Environment setup

Create: `conda env create -f environment.yml`

Activate: `conda activate my_env`

Verify: `conda env list`

Update: Change `requirements.txt` and run  `conda env update --file environment.yml --prune`

Deactivate:  `conda deactivate`

## Install and Update Packages

With environment activated(!):

Install package: `conda install my_package` or `conda install my_package=1.0.0`

Update package: `conda update my_package`

Verify: `conda list`

Remove: `conda remove scipy`

Save current package configuration: `pip freeze > requirements.txt`

## Project Structure

It's convenient to have multiple python files have access to general utility functions and test functions. I find [this](https://xebia.com/blog/a-practical-guide-to-setuptools-and-pyproject-toml/) reference helpful.

I use a `setup.cfg` file at the root level and in an environment run `pip3 install -e .` to install the project modules as a package. `__init__.py` lets code import functions without having to type the entire path.

For testing, I've included a data folder and  a `context.py` file to give tests access to the data.