# Regression

## Introduction

* A regression algorithm is a supervised learning algorithm.
  * The inputs are called *features*
  * The output is called the *label*

* A regression model provides a prediction of a continuous numerical label.

* Spark MLlib provides several regression algorithms:
  * Linear Regression (with Elastic Net, Lasso, and Ridge Regression)
  * Isotonic Regression
  * Decision Tree
  * Random Forest
  * Gradient-Boosted Trees

* Spark MLlib also provides regression algorithms for special types of
continuous numerical labels:
  * Generalized Regression
  * Survival Regression

* Spark MLlib requires the features to be assembled into a vector of doubles column.

