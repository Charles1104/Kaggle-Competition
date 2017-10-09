# Kaggle Competition - Grant Application

Inline-style:
![alt text](https://www.cdc.gov/grants/00_flexslider/images-flexslider-700x540/how-to-apply-slide700x540.png"Logo Title Text 1")

## Short summary

This task requires participants to predict the outcome of grant applications for the University of Melbourne.

## Methodology

I started by cleaning the dataset as it was not amenable for study in the current state. Each row contained 15 columns that were repeated 15 times (225 columns). Each block consisted of information regarding a researcher and each row consisted of one application that included up to 15 researchers.

I started by splitting these blocks and creating a new dataframe with one line per researcher. This made it much easier to  "group by" and create new columns.

I then started to explore each feature (column) and compiled new column from the existing ones. For non-numerical variables, I either got dummies out of it or created categorical variables.

Once I got a proper dataset with valuable columns (close to 100 features in the end), I then applied a random forest model to it. The result was pretty good with a AUC scoring of 94%.

