import sys
sys.path.append('/workspace/heritage-housing-mvp')

import pandas as pd
import joblib


def load_housing_data():
    """
    Path to housing data
    """
    df1 = pd.read_csv("/workspace/heritage-housing-mvp/outputs/datasets/collection/house_prices_records.csv")
    return df1

def load_heritage_data():
    """
    Path to heritage houses dataset
    """
    df2 = pd.read_csv("/workspace/heritage-housing-mvp/outputs/datasets/collection/inherited_houses.csv")
    return df2

def load_housing_cleaned():
    """
    Path to cleaned housing dataset
    """
    df3 = pd.read_csv("/workspace/heritage-housing-mvp/outputs/datasets/collection/HousePricesCleaned.csv")
    return df3
    
def load_pkl_file(file_path):
    """
    Load the machine learning model file
    """
    return joblib.load(filename=file_path)

def load_train_test_data():
    """
    Load train and test data
    """
    X_train = pd.read_csv('/workspace/heritage-housing-mvp/outputs/ml_pipeline/predict_price/v1/X_train.csv')
    X_test = pd.read_csv('/workspace/heritage-housing-mvp/outputs/ml_pipeline/predict_price/v1/X_test.csv')
    y_test = pd.read_csv('/workspace/heritage-housing-mvp/outputs/ml_pipeline/predict_price/v1/y_test.csv')
    y_train = pd.read_csv('/workspace/heritage-housing-mvp/outputs/ml_pipeline/predict_price/v1/y_train.csv')
    return X_train, X_test, y_train, y_test
