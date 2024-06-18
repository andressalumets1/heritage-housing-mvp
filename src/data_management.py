import pandas as pd

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
    
#def load_pkl_files(file_path):
    """
    Load the machine learning model file
    """
