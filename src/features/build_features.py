import sys
import os
import pandas as pd
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from data import make_dataset as mdt

df = pd.read_csv('data/processed/nonait.csv')

#Creating a mean arterial pressure variable.
df['map'] = ((df['diaBP']*2) + df['sysBP'])/3
df['map'] = np.round(df['map'],2)
df.to_csv('data/interim/newfeat.csv',index=False, inplace=True)


