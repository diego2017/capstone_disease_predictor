[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/0GBBWOiF)
## Diabetes risk predictor
=========================

### Project Overview

The project delivers a machine learning solution designed to predict the risk of individuals developing diabetes, using readily accessible health indicators.

Diabetes has become into one of the most significant epidemics in human history, affecting an estimated 422 million people globally, including almost 5 million individuals in the UK. Furthermore, 1 million people in the UK living with diabetes remain undiagnosed. This machine learning solution empowers doctors to identify patients at elevated risk more efficiently, facilitating timely and appropriate interventions.

The potential benefits of this machine learning solution are twofold, encompassing both health and financial aspects:
- Enhanced life expectancy for patients with type 2 diabetes, contingent upon timely and proper treatment
- Financial relief for governments, stemming from the ability to treat patients proactively and mitigate the risk of complications

The target variable in this context categorizes participants as having diabetes, prediabetes, or neither.

The dataset comprises 20 health indicators.

This repository houses Jupyter notebooks, CSV files, and environmental specifications, all of which pertain to a capstone project developed during the BrainStation Data Science bootcamp.


The task is a classification problem, addressed by using Logistic Regression and Random Forest.



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
    - link to copy of the dataset: https://drive.google.com/drive/folders/1ANKR3U_tE03NW3TRwdM0kcI7-l4zCZ2K?usp=drive_link 

* `model`
    - joblib dump of final model / model object

* `notebooks`
    - 01-data-loading-cleaning
    - 02-eda
    - 03-pre-processing
    - 04a-modelling_log_reg_os
    - 04b-modelling_decision_tree_os
    - 04c-modelling_log_reg_no-os copy
    - 04d-modelling_decision_tree_no-os_no-pca
    - 05-findings
    

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