# Introduction

This is a machine learning problem with relatively small dataset. First, by observing the dataset, I found that there is one missing value. Also, it is an unbalanced classification problem. There are only three label '2' in the training dataset out of 54 of them in total.

# Implement missing value

To implement missing value, I used regression method. Since the missing value is in column 'C' and it is very likely to be numerical.

# Handling with imbalanced data

Since there are only three label '2' in the training dataset, I tried to include them all into training dataset for cross-validation. The rest 51 data points are randomly divided into three sets. Each time during cv, I used two sets of them and the data with label '2' (37 in total) to train. The rest is for cv test. It is a three-fold cv, the model performance will be evaluated based on the correctness of all three cv tests.

# Choosing models

I chose widely used classification models in machine learning, including KNN, SVM, Randomforest, NaiveBayes and Decision Tree.

## Decision Tree

In general, we do not need to generalize the dataset. And the decision tree model are intepretable. The correct rate is **27/51**.

## K-Nearest Neighbours

KNN method is very simple to fit, however, KNN is a kind of lazy learning method. In inbalanced dataset, for class with small sample, it may result inaccuracy when adding a new sample into the dataset (less neighbours of small class contribute to it). Also, KNN has tuning parameters 'k' to tune. The correct rate is **37/51** when k=3.

## SVM

SVM method is useful in small datasets. It also works for multiple classification. The correct rate is **43/51**.

# NaiveBayes

NaiveBayes model relies on Bayes Theorem. It is very stable for classification. But a prior distribution is required. The correct rate is **40/51**.

# Randomforest

Randomforest is the best model in cross-validation with correct rate **46/51**. It is efficient for inbalanced data and the training is relatively fast.




