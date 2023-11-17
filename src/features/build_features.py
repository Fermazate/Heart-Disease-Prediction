import sys
import os
import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from data import make_dataset as mdt

df = pd.read_csv('data/processed/nonait.csv')

#Creating a function to run SMOTE analysis for a given variable in a dataframe.
def SMOTE_analysis(df,target):
    #Creating a copy of the dataframe.
    df = df.copy()
    #Splitting the dataframe.
    X = df.drop(df[target],axis=1)
    Y = df[target]
    #Creating SMOTE object
    smote = SMOTE()
    
    #Applying SMOTE
    smote = SMOTE()
    
    #Returning a dataframe with the SMOTE analysis
    return smote_df
#Creating a mean arterial pressure variable.
df['map'] = ((df['diaBP']*2) + df['sysBP'])/3
df['map'] = np.round(df['map'],2)
df.to_csv('data/interim/newfeat.csv',index=False, inplace=True)