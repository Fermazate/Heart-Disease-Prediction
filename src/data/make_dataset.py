import pandas as pd
import matplotlib.pyplot as plt
import sys
from sklearn.experimental import enable_iterative_imputer

sys.path.append('/Users/andresgarciarobles/Documents/Proyectos de ciencia de datos/Heart-Disease-Prediction')

#from src.features.build_features import Itimp, dropfew
import src.features.build_features as bld

df = pd.read_csv('data/raw/framingham.csv')

#Drop rows with Nan values AND that represent <5% of the data.
nona = bld.dropfew(df,'data/interim/dfnona.csv')
nonaknn = bld.knn_replace(df,'data/interim/nonaknn.csv')
nonaIt = bld.Itimp(df,'data/interim/nonait.csv')





