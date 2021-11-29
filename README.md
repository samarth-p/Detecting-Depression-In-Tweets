# Detecting-depression-in-tweets

## Overview
A model to detect depression in tweets. The model was implemented using CNN+LSTM. The trained model was tested on a dataset of COVID-19 related tweets to detect signs of depression.

## Data Gathering

The dataset consists of labeled data, i.e., an equal number of depression indicative tweets
and random tweets (non-depressive). The random tweets dataset was taken from the Kaggle dataset [twitter_sentiment](https://www.kaggle.com/ywang311/twitter-sentiment/data). The [depression tweets](https://www.kaggle.com/samarthp27/depression-dataset) were scraped using TWINT with various depression-related keywords.

## Training

The model was trained with Convolutional Neural Networks (CNN) and Long Short Term Memory (LSTM) using Keras. Several other Machine Learning algorithms such as Logistic Regression, KNN, SVM, and Decision Trees were implemented to compare the accuracies.

## Results

| Algorithm              | Accuracy  |
| ---------------------- | --------- |
| Logistic Regression    | 49.84%    |
| K-Nearest Neighbors    | 68.96%    |
| Decision Tree          | 86.94%    |
| Support Vector Machine | 68.17%    |
| CNN + LSTM             | 97%       |
<br />

## Application on COVID-19 Dataset

The COVID-19 dataset consisted of tweets that were scraped using TWINT with COVID-19 keywords. This dataset can be found [here](https://www.kaggle.com/samarthp27/covid19-tweets). The trained model was tested on this dataset and the results as given below - 

Total number of Tweets: 244198<br />
Number of Depressive Tweets: 133109<br />
Number of Non-Depressive Tweets: 111089<br />
Percentage of Depressive Tweets: 54.51%
