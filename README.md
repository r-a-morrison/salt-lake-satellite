## Project Template

This is a generic repository template primarily intended for data science, but it's fairly generic and can therefore be used for many purposes.

Thanks to Griffin Chure's repository [Reproducible Research](https://github.com/gchure/reproducible_research) for inspiration and education. Much of this repository is based Griffin's repository.

# Outline
* `notes`: Some simple brainstorming of objectives, ideas, and hypotheses. You may want to exclude this from GitHub.
* `executable_code`: Where all of the executed code lives.
    * `exploratory`: A sandbox where you keep a record of your different approaches to transformation, interpretation, cleaning, or generation of data.
    * `processing`: Any code used to transform the data into another type should live here. This can include everything from parsing of text data, image segmentation/filtering, or simulations.
    * `analysis`: Code that draws conclusions from a data set (be it from an experiment, data scraping, or compiled data collection). Analysis may include regression, dimensionality reduction, or calculation of various quantities.
    * `figure_generation`: Any code used to generate figures for your finished work, presentations, or for any other use.
    * It may be preferable to include additional folders here as needed, e.g. `model_training`, `model_testing`, etc.
* `module_code`: Custom code you’ve written that is not executed directly but is called from files in the code directory. If you’ve written your code in Python, for example, this can be the root folder for your custom software module or simply house a file with all of your functions.
* `tests`: All test suites for your code. Any custom code you’ve written should be thoroughly and adequately tested to make sure you know how it is working.
* `raw_data`: Small (< 50 MB) raw data sets, or links to where large data sets are stored. Can be useful to have a ”master” data set separate from processed data to avoid overwriting initial data.
* `processed_data`: Cleaned data sets as well as any other processed data. This directory houses all small (< 50 MB) data sets. This is not a place to store all of your large (> 50 MB) data files, such as images. For accessibility of these large data sets, there are myriad online data repositories such as Zenodo which provide free storage and DOI generation. In addition, you should have all of your data backed up locally with redundancy.
* `figures`: Output figures stored here, not with code.
* `documents`: Final presentable files and LaTeX, etc. used to create documentation
* `LICENSE`: A legal protection of your work. It is important to think deeply about the licensing of your work, and is not a decision to be made lightly. See this useful site for more information about licensing and choosing the correct license for your project.
* `README.md`: A descriptive yet succinct description of your research project and information regarding the structure outlined below. Include software information, computing environment, and dependencies. Also include license information.
