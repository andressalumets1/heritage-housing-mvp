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

