import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

def load_data(file_path):
    """
    Loads data from a CSV file located at 'file_path
    using 'pandas' and returns it as a DataFrame.
    """
    return pd.read_csv(file_path)

def regression_performance(X_train, y_train, X_test, y_test, pipeline):
    """
    Evaluates the performance of a regression model pipeline on both training
    and test datasets. It calls 'regression_evaluation' function to compute and display
    metrics.
    """
    st.subheader("Model Evaluation")
    st.write("* Train Set")
    regression_evaluation(X_train, y_train, pipeline)
    st.write("* Test Set")
    regression_evaluation(X_test, y_test, pipeline)
    st.write("""
    The model effectively fulfilled the client's proposed criteria of R2 = 0.75,
    both on training and test sets.
    """)

def regression_evaluation(X, y, pipeline):
    """
    Computes and displays regression evaluation metrics
    for predictions made by the 'pipeline'.
    """
    prediction = pipeline.predict(X)
    st.write('R2 Score:', r2_score(y, prediction).round(3))
    st.write('Mean Absolute Error:', mean_absolute_error(y, prediction).round(3))
    st.write('Mean Squared Error:', mean_squared_error(y, prediction).round(3))
    st.write('Root Mean Squared Error:', mean_squared_error(y, prediction, squared=False).round(3))
    st.write("\n")

def page_performance_body():
    """
    Constructs a streamlit web application page that displays various sections of
    model performance metrics and details. It loads training and test data, the best
    performing regression pipeline 'best_pipeline_regressor', and visualizations like
    'feature_importance' plot.
    """
    X_train = load_data("outputs/ml_pipeline/predict_price/v1/X_train.csv")
    y_train = load_data("outputs/ml_pipeline/predict_price/v1/y_train.csv")
    X_test = load_data("outputs/ml_pipeline/predict_price/v1/X_test.csv")
    y_test = load_data("outputs/ml_pipeline/predict_price/v1/y_test.csv")
    best_pipeline_regressor = joblib.load("outputs/ml_pipeline/predict_price/v1/regression_pipeline.pkl")
    feature_importance = plt.imread('outputs/ml_pipeline/predict_price/v1/feature_importance.png')

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

    st.header("* Conclusion")
    st.write("""
    In this project, it was developed a robust machine learning pipeline to predict house 
    prices using various regression models. It was started by implementing extensive data 
    cleaning and feature engineering steps. The core of the project involved hyperparameter 
    optimization through GridSearchCV, where it was tested multiple models and 
    configurations to identify the best-performing model.

    The Gradient Boosting Regressor initially showed promising results, 
    but further optimization revealed that the Extra Trees Regressor with specific 
    hyperparameters provided the best performance, exceeding the business requirement 
    of an R2 score of at least 0.75 on both the training and test sets. 
    It was identified the most influential features and refit the model using these key 
    predictors. Finally, the optimized model and relevant datasets were saved for 
    future use.

    This structured approach not only ensured the creation of an accurate and reliable 
    predictive model but also highlighted the importance of feature selection and model 
    tuning in achieving superior performance. The project demonstrates the effectiveness 
    of a systematic ML pipeline in solving realworld regression problems.
    """)