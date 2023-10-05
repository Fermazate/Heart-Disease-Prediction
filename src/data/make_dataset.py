import sys
import os
import pandas as pd
import logging
import argparse

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

import src.features.build_features as bld

df = pd.read_csv('data/raw/framingham.csv')


#Drop rows with Nan values AND that represent <5% of the data.
nona = bld.dropfew(df,'data/interim/dfnona.csv')
nonaknn = bld.knn_replace(nona,'data/processed/nonaknn.csv','glucose')
nonaIt = bld.iterative_impute(nona,'data/processed/nonait.csv')
knnacc = bld.validate_imputation_accuracy(nona,'glucose')
itacc = bld.validate_iterative_imputation_accuracy(nona,'glucose')
