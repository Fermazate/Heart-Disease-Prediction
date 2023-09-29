import pandas as pd
import matplotlib.pyplot as plt

from sklearn.impute import KNNImputer, IterativeImputer

import warnings
warnings.filterwarnings('ignore')

def dropfew(data, dir, save = True, ind = False):
    #Drop all the rows with missing values with no normal distributions and are less than 5% of total data.
    data = pd.DataFrame(data)
    columns_withna = [var for var in data.columns if data[var].isnull().mean() < 0.05 and data[var].isnull().mean() > 0]
    data.dropna(subset=columns_withna, inplace=True)
    if save == True:
        data.to_csv(dir,index = ind)
    return data
        
def knn_replace (data, dir, save = True, ind = False):
    #Replace missing values of glucose (Not <5% of total values) with multivariate imputation.  
    data = pd.DataFrame(data)
    knn_imp = KNNImputer(n_neighbors=2)
    data = pd.DataFrame(knn_imp.fit_transform(data), columns=data.columns)
    if save == True:
        data.to_csv(dir,index=ind)
    return data

def Itimp(data,dir,save = True,ind = False):
    """_summary_

    Args:
        data (pandas.core.frame.DataFrame): A pandas database.
        dir (string): Directory to save.

    Returns:
        pandas.core.frame.DataFrame: Return a pandas dataframe with processed information
    """
    data = pd.DataFrame(data)
    itimp = IterativeImputer()
    data = pd.DataFrame(itimp.fit_transform(data),columns=data.columns)
    if save == True:
        data.to_csv(dir, index = ind)
    return data