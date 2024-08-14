# Decision Tree Model for Classification and Analysis of Customer Fault Trends

This project involves training a decision tree model using provided CSV data files to predict whether certain rows meet specific criteria (i.e., whether they need to be worked upon further or not) . The code preprocesses the data, trains a model, evaluates it, and generates visualizations for better understanding.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Arguments](#arguments)
- [Outputs](#outputs)
- [Visualizations](#visualizations)
- [Acknowledgments](#acknowledgments)

## Features

- *Data Preprocessing*: Cleans and processes input CSV files, including handling missing values, filtering rows, and encoding categorical data.
- *Feature Engineering*: Generates additional features such as Above_Threshold, Passed_Percentage, and Blocked_Failed_Percentage to improve model performance.
- *Model Training*: Utilizes a Decision Tree Classifier with customizable parameters to fit the training data.
- *Model Evaluation*: Evaluates the model on test data and computes accuracy.
- *Visualization*: Generates and saves various plots including the decision tree diagram, feature importance, and others.

## Requirements

- Python 3.x
- Required Python libraries:
  - pandas
  - numpy
  - scikit-learn
  - matplotlib
  - seaborn
  - argparse

## Installation

1. Install the required libraries:
   bash
   pip install -r requirements.txt
   

## Usage

To run the script, use the command below, specifying paths to your training and testing CSV files:

bash
python
python model.py <threshold> <file_path_1> <file_path_2> <file_path_3>...


## Arguments

- threshold_multiplier: Multiplier for the mean threshold used to create the Above_Threshold feature. Default is 0.1.
- ⁠- file_paths: List of paths to the CSV files for prediction.

## Outputs

The script generates the following outputs:

1. *Decision Tree Diagram*: decision_tree.png
2. *Feature Importance Plot*: feature_importance.png
3. *Bar Plot of Not Recommended Rows*: not_recommended_counts.png
4. *Scatter Plot of Grand Total vs Blocked_Failed_Percentage*: grand_total_vs_blocked_failed.png
5. *Box Plot of Blocked_Failed_Percentage by Recommendation Status*: blocked_failed_by_recommendation.png
6. *Summary File*: summary.txt - A text file containing a summary of the evaluation results, including the number of recommended and not recommended rows, along with accuracy for each test file.

## Visualizations

### 1. Decision Tree Diagram

The decision tree model's structure is saved as decision_tree.png. This file visualizes how the model makes decisions based on the input features.

### 2. Feature Importance Plot

A bar plot showing the importance of each feature used in the decision tree model is saved as feature_importance.png.

### 3. Bar Plot of Not Recommended Rows

A bar plot displaying the number of not recommended rows per source file is saved as not_recommended_counts.png.

### 4. Scatter Plot of Grand Total vs Blocked_Failed_Percentage

A scatter plot showing the relationship between Grand Total and Blocked_Failed_Percentage with points colored based on the model's predictions is saved as grand_total_vs_blocked_failed.png.

### 5. Box Plot of Blocked_Failed_Percentage by Recommendation Status

A box plot visualizing the distribution of Blocked_Failed_Percentage for recommended and not recommended rows is saved as blocked_failed_by_recommendation.png.

## Acknowledgments

This project leverages Python's powerful data science libraries to perform classification and generate insights from data. Special thanks to the open-source community for their contributions to these libraries.
