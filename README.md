
# Churn Prediction

## Table of Contents

- Project Background
- Author
- Data Source
- Libraries Used
- Motivation for The Project
- Files
- Summary of the results
- Acknowledgment
- Data Source
- Known errors (updated)

---- 

### Project Background

Measure the churn, design metrics for forecasting churn, and build a predictive machine learning model. This project provide an end to end working solution to a churn problem based on user’s raw event log data.

For full article explaining this project, link below: 

[https://weimingchenzero.medium.com/applied-data-science-with-churn-problem-a778821577a2][1]

---- 

### Author

Weiming Chen (Alan)

---- 

### Data Source (Event Log Data)
- (mini 120MB) s3n://udacity-dsnd/sparkify/mini\_sparkify\_event\_data.json
- (full 12GB) s3n://udacity-dsnd/sparkify/sparkify\_event\_data.json

---- 

### Libraries / Environments

Python 3.9
PyCharm
Jupyter
Pandas
Numpy
Plotly
Matplotlib
Scikit-learn
XGBoost

---- 

### Motivation for The Project

Churn problem is crucial for consumer business industry. Churn means losing users, reducing revenue. A churn predictive model can help us forecasting churn, understanding the factors behind, and seizing the best opportunities and timing to retain customers. 

---- 

### Files

Please note that GitHub won’t display Plotly visualization in Jupyter source code notebook file viewing. For a better reading experience, please check the exported PDF file. 

Source Code:
- sparkify_min.ipynb_

Exported versions for reading
- sparkify_min.pdf_
- sparkify_min.html 

---- 

### Summary of the results

Logistic Regression scored 0.73
XGBoost scored 0.84

XBGoost is able to detect 7 of 10 actual churn instants in test set, while Logistic Regression detect 1 of 10.


---- 

### Acknowledgment
- Metric Cohort Plot function snippet from book ‘Fight Churn’
- Data provided by Udacity


### Data Source (Event Data)
- (mini 120MB) s3n://udacity-dsnd/sparkify/mini\_sparkify\_event\_data.json
- (full 12GB) s3n://udacity-dsnd/sparkify/sparkify\_event\_data.json

### Known errors (updated)
A possible mistake made in Logistic Regression section that, I used the normalized values that was applying scaler on whole set. Instead should scaler fit to train set, and then transform with train and set separately with that returned scaler.

Should be something like: 
```
# preprocessing using 0-1 scaling
scaler = MinMaxScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```
then send to training (fit and predict)

(notebook codes didn't update. lazy. :-) )




[1]:	https://weimingchenzero.medium.com/applied-data-science-with-churn-problem-a778821577a2