import streamlit as st
import pandas as pd
from src.data_management import load_pkl_file, load_heritage_data, load_housing_data
from datetime import date
from src.machine_learning.predictive_analysis_ui import predict_price, predict_inherited_house_price

def page_predict_body():

    version = 'v1'
    regression_pipe = load_pkl_file("/workspace/heritage-housing-mvp/outputs/ml_pipeline/predict_price/v1/regression_pipeline.pkl")
    house_features = (pd.read_csv("/workspace/heritage-housing-mvp/outputs/ml_pipeline/predict_price/v1/X_train.csv")
                                    .columns
                                    .to_list()
                                    )

    st.header("Inherited House Sale Price Prediction")
    st.info("""
    **Business Requirement 2:** The client is interested in predicting the house sale prices
    from her 4 inherited houses, and any other house in Ames, Iowa.
    """)

    X_inherited = load_heritage_data()

    summed_price = 0
    predicted_sale_price = []
    for i in range(X_inherited.shape[0]):
        pprice = predict_inherited_house_price(X_inherited.iloc[[i,]], house_features, regression_pipe)
        predicted_sale_price.append(round(pprice))
        summed_price = summed_price + pprice
        summed_price = round(summed_price)
    X_inherited = X_inherited.filter(house_features)
    X_inherited['PredictedSalePrice'] = predicted_sale_price
    st.write(X_inherited.head())
    st.write(f"* Summed price: **${summed_price}** \n"
            f"* Features used: **{X_inherited.columns.to_list()[:-1]}**.\n"
                f"Summed value of 4 inherited houses."
            )

    st.write("---")

    X_live = DrawInputsWidgets()

    if st.button("Predict Sale Price"):
        price_prediction = predict_price(X_live, house_features, regression_pipe)

        if price_prediction == 1:
            predict_price(X_live, house_features, regression_pipe)

def  check_variables_for_UI(house_features):
    st.write(f"* There are {len(house_features)} features for the UI: \n\n {house_features}")

def DrawInputsWidgets():
    df = load_housing_data()
    
    percentageMin, percentageMax = 0.4, 2.0

    col1, col2, col3, col4 = st.beta_columns(4)
    col5, col6, col7, col8 = st.beta_columns(4)
    
    X_live = pd.DataFrame([], index=[0])

    with col1:
            feature = "GarageArea"
            st_widget = st.number_input(
                    label= feature,
                    min_value = int(df[feature].min()*percentageMin),
                    max_value = int(df[feature].max()*percentageMax),
                    value = int(df[feature].median()),
        step = 50
            )

    X_live[feature] = st_widget

    with col2:
            feature = "GrLivArea"
            st_widget = st.number_input(
                    label = feature,
                    min_value = int(df[feature].min()*percentageMin),
                    max_value = int(df[feature].max()*percentageMax),
                    value = int(df[feature].median()),
        step = 50
            )
    
    X_live[feature] = st_widget

    with col3:
            feature = "OverallQual"
            st_widget = st.number_input(
                    label = feature,
                    min_value = 1,
                    max_value = 10,
                    value = 5,
        step = 1
            )
    
    X_live[feature] = st_widget

    with col4:
            feature = "TotalBsmtSF"
            st_widget = st.number_input(
                    label = feature,
                    min_value = int(df[feature].min()*percentageMin),
                    max_value = int(df[feature].max()*percentageMax),
                    value = int(df[feature].median()),
        step = 50
                    )

    X_live[feature] = st_widget

    with col5:
            feature = "YearBuilt"
            st_widget = st.number_input(
                    label = feature,
                    min_value = int(df[feature].min()*percentageMin),
                    max_value = date.today().year,
                    value = int(df[feature].median()),
        step = 1
                    )
    
    X_live[feature] = st_widget

    return X_live

    
    