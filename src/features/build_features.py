import pandas as pd
import matplotlib.pyplot as plt

from sklearn.impute import KNNImputer

import warnings
warnings.filterwarnings('ignore')
#Open database.
df = pd.read_csv('data/raw/framingham.csv')

#Drop all the rows with missing values with no normal distributions and are less than 5% of total data.
columns_withna = [var for var in df.columns if df[var].isnull().mean() < 0.05 and df[var].isnull().mean() > 0]
df.dropna(subset=columns_withna, inplace=True)

#Replace missing values of glucose (Not <5% of total values) with multivariate imputation.
knn_imp = KNNImputer(n_neighbors=2)
df2 = pd.DataFrame(knn_imp.fit_transform(df), columns=df.columns)


#register new dataframe in an csv archive.
df.to_csv('data/interim/dfnona.csv', index=False)
df2.to_csv('data/interim/dfknn.csv', index=False)

