import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_management import load_pkl_file
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np

st.set_page_config(page_title="ML Pipeline Performance", layout="wide")

def load_data(file_path):
    return pd.read_csv(file_path)

X_train = load_data("/workspace/heritage-housing-mvp/outputs/ml_pipeline/predict_price/v1/X_train.csv")
y_train = load_data("/workspace/heritage-housing-mvp/outputs/ml_pipeline/predict_price/v1/y_train.csv")
X_test = load_data("/workspace/heritage-housing-mvp/outputs/ml_pipeline/predict_price/v1/X_test.csv")
y_test = load_data("/workspace/heritage-housing-mvp/outputs/ml_pipeline/predict_price/v1/y_test.csv")
best_pipeline_regressor = joblib.load("/workspace/heritage-housing-mvp/outputs/ml_pipeline/predict_price/v1/regression_pipeline.pkl")

st.title("ML Pipeline Performance Dashboard")
st.header("Data Overview")
st.write("### Training Data")
st.write(X_train.head())
st.write("### Test Data")
st.write(X_test.head())

st.header("Model Performance Metrics")

def regression_performance(X_train, y_train, X_test, y_test, pipeline):
    st.subheader("Model Evaluation")
    st.write("* Train Set")
    regression_evaluation(X_train, y_train, pipeline)
    st.write("* Test Set")
    regression_evaluation(X_test, y_test, pipeline)

def regression_evaluation(X, y, pipeline):
    prediction = pipeline.predict(X)
    st.write('R2 Score:', r2_score(y, prediction).round(3))
    st.write('Mean Absolute Error:', mean_absolute_error(y, prediction).round(3))
    st.write('Mean Squared Error:', mean_squared_error(y, prediction).round(3))
    st.write('Root Mean Squared Error:', np.sqrt(mean_squared_error(y, prediciton)).round(3))
    st.write("\n")

regression_performance(X_train, y_train, X_test, y_test, best_pipeline_regressor)

st.header("Feature Importance")
df_feature_importance = pd.read_csv()