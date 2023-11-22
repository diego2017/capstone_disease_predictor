
# Diabetes early warning system 
=========================

### Project and solution overview
Problem:
The problem tackled by this project is that a large number of people who have diabetes, have not being diagnosed and therefore, are not being treated accordingle. 

Solution:
The solution proposed is to leverage machine learning to create an early warning system that can be used by medical professionals to identify patients with a high risk of developing diabetes, using readily accessible health indicators.

Deep-dive into problem and solution:
Diabetes has become into one of the most significant epidemics in human history, affecting an estimated 422 million people globally, including almost 5 million individuals in the UK. Furthermore, 1 million people in the UK living with diabetes remain undiagnosed. This machine learning solution empowers doctors to identify patients at elevated risk more efficiently, facilitating timely and appropriate interventions.

The potential benefits of this machine learning solution are twofold, encompassing both health and financial aspects:
- Enhanced life expectancy for patients with type 2 diabetes, contingent upon timely and proper treatment
- Financial relief for governments, stemming from the ability to treat patients proactively and mitigate the risk of complications


### Dataset

The dataset used to train and test the models developed in this project is derived from The Behavioral Risk Factor Surveillance System (BRFSS), which is a health-related telephone survey collected annually by the CDC (The Centers for Disease Control and Prevention).

The specific dataset used was consolidated and shared by Alex Teboul. It cound be found on the following page:
Diabetes Health Indicators Dataset
 (https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset/data?select=diabetes_binary_5050split_health_indicators_BRFSS2015.csv).

The target variable in this context categorizes participants as having diabetes, prediabetes, or neither.

The dataset comprises 20 health indicators.

The following table provides an overview of all data features found in the original dataset:

| Column                       | Data Type | Description                                                                                                      | Possible Values                                          |
|------------------------------|-----------|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| TARGET VARIABLE: Diabetes_012| float64   | Does the participant have diabetes or prediabetes                                                                | 0 = no diabetes, 1 = prediabetes, 2 = diabetes           |
| HighBP                       | float64   | Has the participant being told by a medical professional that they have high blood pressure                      | 0 = no high BP, 1 = high BP                              |
| HighChol                     | float64   | Has the participant being told by a medical professional that they have high blood cholesterol                   | 0 = no high cholesterol, 1 = high cholesterol           |
| CholCheck                    | float64   | Has the participant cholesterol been checked in the last 5 years                                                 | 0 = no cholesterol check in 5 years, 1 = yes             |
| BMI                          | float64   | The Body Mass Index (BMI) of the participant                                                                     | Any number from 12 to 98                                 |
| Smoker                       | float64   | Has the participant smoked at least 100 cigarettes in their entire life                                          | 0 = no, 1 = yes                                          |
| Stroke                       | float64   | Has the participant ever had a stroke                                                                            | 0 = no, 1 = yes                                          |
| HeartDiseaseorAttack         | float64   | Has the participant has had a Coronary Heart Disease (CHD) or myocardial infarction (MI)                         | 0 = no, 1 = yes                                          |
| PhysActivity                 | float64   | Has the participant done any physical activity in past 30 days                                                   | 0 = no, 1 = yes                                          |
| Fruits                       | float64   | Does the participant consume at least 1 fruit per day                                                            | 0 = no, 1 = yes                                          |
| Veggies                      | float64   | Does the participant consume vegetables at least once per day                                                    | 0 = no, 1 = yes                                          |
| HvyAlcoholConsump            | float64   | Does the participant consume 14 drinks or more per week if they are an adult male, or 7 drinks or more per week  | 0 = no, 1 = yes                                          |
| AnyHealthcare                | float64   | Does the participant have any kind of health care coverage                                                       | 0 = no, 1 = yes                                          |
| NoDocbcCost                  | float64   | Has the participant had the need to see a doctor in the past 12 months but could not due to financial reasons?   | 0 = no, 1 = yes                                          |
| GenHlth                      | float64   | How does the participant describe their health levels on a scale from 1 to 5                                     | 1 = excellent, 2 = very good, 3 = good, 4 = fair, 5 = poor|
| MentHlth                     | float64   | How many days of bad mental health has the participant had in the last 30 days                                   | 1 to 30                                                  |
| PhysHlth                     | float64   | How many days has the participant experienced physical illness or an injury in the last 30 days                  | 1 to 30                                                  |
| DiffWalk                     | float64   | Does the participant have serious difficulty walking or climbing stairs                                          | 0 = no, 1 = yes                                          |
| Sex                          | float64   | What gender was the participant assigned at birth                                                                | 0 = female, 1 = male                                     |
| Age                          | float64   | Group age of the participant                                                                                     | 1 to 13 (age groups detailed in the table)               |
| Education                    | float64   | The maximum level of education of the participant                                                                | 1 to 6 (education levels detailed in the table)          |
| Income                       | float64   | Income level of the participant                                                                                  | 1 to 8 (income ranges detailed in the table)             |



### Walkthrough Demo

...
...
...

### Project Flowchart

...
...
...

### Project Organization



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