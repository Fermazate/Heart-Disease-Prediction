import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from data import make_dataset as mdt

df = pd.read_csv('data/processed/nonait.csv')

#Creating a mean arterial pressure variable.
df['map'] = ((df['diaBP']*2) + df['sysBP'])/3
mdt.save_dataset(df,'data/processed/dfnew.csv')


