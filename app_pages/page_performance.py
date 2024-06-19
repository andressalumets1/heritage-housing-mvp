import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

def load_data(file_path):
    return pd.read_csv(file_path)

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
    st.write('Root Mean Squared Error:', mean_squared_error(y, prediction, squared=False).round(3))
    st.write("\n")

def page_performance_body():
    X_train = load_data("/workspace/heritage-housing-mvp/outputs/ml_pipeline/predict_price/v1/X_train.csv")
    y_train = load_data("/workspace/heritage-housing-mvp/outputs/ml_pipeline/predict_price/v1/y_train.csv")
    X_test = load_data("/workspace/heritage-housing-mvp/outputs/ml_pipeline/predict_price/v1/X_test.csv")
    y_test = load_data("/workspace/heritage-housing-mvp/outputs/ml_pipeline/predict_price/v1/y_test.csv")
    best_pipeline_regressor = joblib.load("/workspace/heritage-housing-mvp/outputs/ml_pipeline/predict_price/v1/regression_pipeline.pkl")
    feature_importance = plt.imread('/workspace/heritage-housing-mvp/outputs/ml_pipeline/predict_price/v1/feature_importance.png')

    st.title("ML Pipeline Performance Dashboard")
    st.header("Data Overview")
    st.write("### Training Data")
    st.write(X_train.head())
    st.write("### Test Data")
    st.write(X_test.head())

    st.header("Model Performance Metrics")
    regression_performance(X_train, y_train, X_test, y_test, best_pipeline_regressor)

    # show best features
    st.header("* The features the model was trained on and their importance")
    st.write(X_train.columns.to_list())

    st.image(feature_importance, caption='Feature Importance')
    st.write("---")

    # show pipeline steps
    st.header("* ML pipeline to predict sales prices of houses")
    st.code(best_pipeline_regressor)
    st.write("---")