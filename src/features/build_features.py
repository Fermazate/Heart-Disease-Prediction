import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.experimental import enable_iterative_imputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier

import warnings
warnings.filterwarnings('ignore')
#Open database.
df = pd.read_csv('data/raw/framingham.csv')

#Drop all the rows with missing values with no normal distributions and are less than 5% of total data.
columns_withna = [var for var in df.columns if df[var].isnull().mean() < 0.05 and df[var].isnull().mean() > 0]
df.dropna(subset=columns_withna, inplace=True)
df2 = df

#Replace missing values of glucose (Not <5% of total values) with multivariate imputation.
knn_imp = KNNImputer(n_neighbors=2)
df2 = knn_imp.fit_transform(df2)

#register new dataframe in an csv archive.
df.to_csv('data/interim/dfnona.csv', index=False)
df2.to_csv('data/interim/dfknn.csv', index=False)

