Breast Cancer Diagnosis Project
Welcome to the Breast Cancer Diagnosis Project! This project aims to predict whether a breast cancer diagnosis is malignant or benign based on the physical characteristics of the tumor. The project uses a dataset of breast cancer tumor features and applies machine learning techniques to build a predictive model.

Table of Contents
Introduction
Data Description
Data Preprocessing
Exploratory Data Analysis
Model Selection
Results and Discussion
Conclusion
How to Run the Program
Directory Structure
References
Introduction
Breast cancer is one of the most common cancers among women worldwide. Early diagnosis and treatment are crucial for improving survival rates. This project leverages machine learning techniques to build a model that can accurately classify breast cancer tumors as malignant or benign based on their physical characteristics.

Data Description
The dataset used in this project is sourced from the UCI Machine Learning Repository. It contains 569 rows and 33 columns, where each row represents a patient and each column represents a different feature of the patient's diagnosis.

Key Features
id: Unique identifier for each patient
diagnosis: Diagnosis (M = malignant, B = benign)
radius_mean: Mean of distances from center to points on the perimeter
texture_mean: Standard deviation of gray-scale values
perimeter_mean: Perimeter of the tumor
area_mean: Area of the tumor
smoothness_mean: Local variation in radius lengths
compactness_mean: Perimeter^2 / area - 1.0
concavity_mean: Severity of concave portions of the contour
concave points_mean: Number of concave portions of the contour
symmetry_mean: Symmetry of the tumor
fractal_dimension_mean: "Coastline approximation" - 1
The last column, Unnamed: 32, is empty and can be dropped.

Data Preprocessing
Steps Taken:
Handling Missing Values: The dataset was checked for missing values, and appropriate measures were taken.
Data Normalization: Features were normalized to ensure uniformity.
Feature Selection: Irrelevant features were dropped, including the Unnamed: 32 column.
Exploratory Data Analysis
Exploratory Data Analysis (EDA) was conducted to gain insights into the data. Visualizations and statistical analyses were performed to understand the distribution of features and identify correlations. Key findings from the EDA include the identification of important features that are indicative of malignancy.


Model Selection
Several machine learning models were considered, including Logistic Regression, Decision Trees, and Support Vector Machines. After comparing their performance, Logistic Regression was selected due to its interpretability and high accuracy.

Results and Discussion
The Logistic Regression model achieved high accuracy in classifying tumors as malignant or benign. The model's performance was evaluated using metrics such as accuracy, precision, recall, and F1 score. The most important features for diagnosis were identified, providing valuable insights for medical practitioners.
