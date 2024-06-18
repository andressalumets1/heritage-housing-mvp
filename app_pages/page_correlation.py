import streamlit as st
from src.data_management import load_housing_cleaned
import matplotlib.pyplot as plt
import seaborn as sns
import ppscore as pps
sns.set_style("whitegrid")
import numpy as np
import plotly.express as px
from feature_engine.encoding import OneHotEncoder

def preprocess_data(df):
    encoder = OneHotEncoder(variables=df.columns[df.dtypes == 'object'].to_list(), drop_last=False)
    df_ohe = encoder.fit_transform(df)
    return df_ohe

def calculate_corr_pps(df_ohe):
    df_corr_spearman = df_ohe.corr(method="spearman")
    df_corr_pearson = df_ohe.corr(method="pearson")
    pps_matrix_raw = pps.matrix(df_ohe)
    pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(columns='x', index='y', values='ppscore')
    return df_corr_spearman, df_corr_pearson, pps_matrix

def heatmap_corr(df, threshold, figsize, font_annot):
    mask = np.zeros_like(df, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    mask[abs(df) < threshold] = True
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(df, annot=True, mask=mask, cmap='viridis', annot_kws={"size": font_annot}, ax=ax, linewidth=0.5)
    plt.ylim(len(df.columns), 0)
    st.pyplot(fig)

def heatmap_pps(df, threshold, figsize, font_annot):
    mask = np.zeros_like(df, dtype=np.bool)
    mask[abs(df) < threshold] = True
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(df, annot=True, mask=mask, cmap='rocket_r', annot_kws={"size": font_annot}, linewidth=0.05, linecolor='grey')
    plt.ylim(len(df.columns), 0)
    st.pyplot(fig)

def page_correlation_body():
    """
    Display the correlated features.
    """
    df3 = load_housing_cleaned()
    df_ohe = preprocess_data(df3)
    df_corr_spearman, df_corr_pearson, pps_matrix = calculate_corr_pps(df_ohe)

    st.header("""Housing prices correlation study""")
    st.info("""
    **BR1:** - The client is interested in knowing how house 
    attributes correlate with sale prices.
    """)
    st.write("""
    A correlation study was conducted to understand how the variables
    are correlated to sale price of a property. With the result the first business
    requirement was addressed. The result showed 11 results since of the encoding technique
    used before making the correlation study, where KitchenQual_Ex and KitchenQual_Gd both
    were included in the list of most correlated features to SalePrice. Therefore
    KitchenQuality Ex/Gd in general can be seen as high importance.
    The result of the correlation study showed that the most correlated variables
    to the Sale Price are:

    1. OverallQual
    2. GrLivArea
    3. YearBuilt
    4. GarageArea
    5. TotalBsmtSF
    6. 1stFlrSF
    7. YearRemodAdd
    8. GarageYrBlt
    9. KitchenQual
    10. OpenPorchSF
    """)


    st.subheader("Visualizations")
    if st.checkbox("Heatmaps: Spearman, Pearson and PPS Correlations"):
        corr_threshold = 0.4
        pps_threshold = 0.4
        figsize = (12, 10)
        font_annot = 10
        st.subheader("Heatmaps: Spearman, Pearson and PPS Correlations")
        st.write("Spearman Correlation Heatmap")
        heatmap_corr(df_corr_spearman, corr_threshold, figsize, font_annot)
        st.write("Pearson Correlation Heatmap")
        heatmap_corr(df_corr_pearson, corr_threshold, figsize, font_annot)
        st.write("PPS Heatmap")
        heatmap_pps(pps_matrix, pps_threshold, figsize, font_annot)


    if st.checkbox("House Prices per Variable"):
        house_price_per_variable(df3)

    if st.checkbox("Distribution of Variable"):
        plot_target_hist(df3, 'SalePrice')

page_correlation_body()



