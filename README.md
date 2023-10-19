[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/0GBBWOiF)
## Diabetes risk predictor
=========================

### Project Overview
This repository contains Jupyter notebooks, CSV files, and environment specifications related to a capstone project developed as part of the BrainStation Data Science bootcamp. 

The project is a prediction tool to identify individuals with a higher risk of developing Diabetes or Pre-diabetes based on basic health indicators.



### Walkthrough Demo

...
...
...

### Project Flowchart

...
...
...

### Project Organization

...
...
...

* `data` 
    - contains link to copy of the dataset (stored in a publicly accessible Google Drive folder)
    - saved copy of aggregated / processed data as long as those are not too large (> 10 MB)

* `model`
    - joblib dump of final model / model object

* `notebooks`
    - 01-data-loading-cleaning
    - 02-eda
    - 03-pre-processing
    - 04-modelling

* `reports`
    - contains final report which summarises the project

* `references`
    - contains papers / tutorials used in the project

* `src`
    - Contains the project source code (refactored from the notebooks)

* `.gitignore`
    - Part of Git, includes files and folders to be ignored by Git version control.
        data/
        references/
        .ipynb_checkpoints

* `capstine_env.yml`
    - Conda environment specification

* `Makefile`
    - Automation script for the project

* `README.md`
    - Project landing page (this page)

* `LICENSE`
    - Project license

### Dataset
Datasets created and used in this project can be found in the following Google drive:
https://drive.google.com/drive/folders/1ANKR3U_tE03NW3TRwdM0kcI7-l4zCZ2K?usp=sharing 

### Credits & References
The data used for this project is from the Behavioral Risk Factor Surveillance System (BRFSS) survey done by the Centers for Disease Control and Prevention. 

The specific dataset used was collected and made available online by Alex Teboul. This collected dataset can be found here: https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset/data?select=diabetes_binary_5050split_health_indicators_BRFSS2015.csv   

--------