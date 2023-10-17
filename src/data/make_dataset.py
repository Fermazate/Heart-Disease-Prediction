import sys
import os
import pandas as pd
import logging
import argparse
from sklearn.experimental import enable_iterative_imputer

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from features import clean_data as bld

def process_data(input_path,interim_path,processed_path):
    
    df = pd.read_csv(input_path)
    
    #Drop rows with Nan values AND that represent <5% of the data.
    nona = bld.dropfew(df, os.path.join(interim_path,'dfnona.csv'))
    bld.knn_replace(nona,os.path.join(processed_path,'nonaknn.csv'),'glucose')
    bld.iterative_impute(nona,'data/processed/nonait.csv')
    knnacc = bld.validate_imputation_accuracy(nona,'glucose')
    itacc = bld.validate_iterative_imputation_accuracy(nona,'glucose')
    
    logging.info(f"KNN Imputation Accuracy (MAE): {knnacc}")
    logging.info(f"Iterative Imputation Accuracy (MAE): {itacc}")
    
    
def main(args):
    """
    Main function to set up logging and initiate data processing.
    """
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    
    process_data(args.input, args.interim, args.processed)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process raw data for Heart Disease Prediction.")
    parser.add_argument('--input', default='data/raw/framingham.csv', help='Path to the raw data file.')
    parser.add_argument('--interim', default='data/interim', help='Path to save interim data.')
    parser.add_argument('--processed', default='data/processed', help='Path to save processed data.')
    
    args = parser.parse_args()
    main(args)
    