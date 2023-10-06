import pandas as pd
import numpy as np

from sklearn.impute import KNNImputer, IterativeImputer
from sklearn.metrics import mean_absolute_error

import warnings
warnings.filterwarnings('ignore')


def dropfew(data, file_path, save=True, ind=False):
    """
    Drop rows with missing values in columns where the missing data is less than 5% of the total data.
    
    Args:
        data (DataFrame): Input data.
        file_path (str): Path to save the input data (if save is True).
        save (bool): Whether to save the modified data to a CSV file.
        ind (bool): Whether to include the index when saving to CSV.
        
    Returns:
        DataFrame: Data with specified rows dropped.
    """
    columns_withna = [var for var in data.columns if data[var].isnull().mean() < 0.05 and data[var].isnull().mean() > 0]
    data.dropna(subset=columns_withna, inplace=True)
    if save:
        data.to_csv(file_path, index=ind)
    return data


def knn_replace(data, file_path, column, save=True, ind=False, decimals=2, n_neighbors=2, weights='uniform'):
    """
    Perform KNN imputation on a specified column of the input data.
    
    Args:
        data (DataFrame): Input data.
        file_path (str): Path to save the input data (if save is True).
        column (str): Column name to perform imputation on.
        save (bool): Whether to save the imputed data to a CSV file.
        ind (bool): Whether to include the index when saving to CSV.
        decimals (int): Number of decimal places to round to after imputation.
        n_neighbors (int): Number of neighbors to use for KNN imputation.
        weights (str): Weight function used in prediction for KNN imputation.
        
    Returns:
        DataFrame: Data with imputed values.
    """
    if column not in data.columns:
        raise ValueError(f"'{column}' not found in the data columns")
    
    knn_imp = KNNImputer(n_neighbors=n_neighbors, weights=weights, metric='nan_euclidean')
    data[column] = knn_imp.fit_transform(data[[column]])
    data[column] = np.round(data[column], decimals=decimals)
    
    if save:
        data.to_csv(file_path, index=ind)
    return data

def _select_validation_data(data, column, fraction=0.2, random_state=None):
    """
    Helper function to select a subset of data for validation.
    """
    known_data = data.dropna(subset=[column])
    missing_idx = known_data.sample(frac=fraction, random_state=random_state).index
    true_values = known_data.loc[missing_idx, column]
    data.loc[missing_idx, column] = np.nan
    return data, true_values, missing_idx

def validate_imputation_accuracy(data, column, fraction=0.2, random_state=None, **knn_params):
    """
    Validate the accuracy of KNN imputation.
    """
    data, true_values, missing_idx = _select_validation_data(data, column, fraction, random_state)
    imputed_data = knn_replace(data, None, column, save=False, **knn_params)
    imputed_values = imputed_data.loc[missing_idx, column]
    mae = mean_absolute_error(true_values, imputed_values)
    return mae


def validate_iterative_imputation_accuracy(data, column, fraction=0.2, random_state=None, **iter_params):
    """
    Validate the accuracy of Iterative Imputation.
    """
    data, true_values, missing_idx = _select_validation_data(data, column, fraction, random_state)
    imp = IterativeImputer(**iter_params)
    data[column] = imp.fit_transform(data[[column]])
    imputed_values = data.loc[missing_idx, column]
    mae = mean_absolute_error(true_values, imputed_values)
    return mae

def iterative_impute(data, file_path, save=True, ind=False):
    """
    Perform Iterative Imputation on the input data.
    
    Args:
        data (DataFrame): Input data.
        file_path (str): Path to save the input data (if save is True).
        save (bool): Whether to save the imputed data to a CSV file.
        ind (bool): Whether to include the index when saving to CSV.
        
    Returns:
        DataFrame: Data with imputed values.
    """
    itimp = IterativeImputer()
    data = pd.DataFrame(itimp.fit_transform(data), columns=data.columns)
    if save:
        data.to_csv(file_path, index=ind)
    return data