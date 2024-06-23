import streamlit as st
from src.data_management import load_housing_cleaned
import matplotlib.pyplot as plt
import seaborn as sns
import ppscore as pps
import numpy as np
import plotly.express as px
from feature_engine.encoding import OneHotEncoder

sns.set_style("whitegrid")

@st.cache
def preprocess_data(df):
    """
    Preprocesses the data by performing One-Hot Encoding on categorical variables.
    """
    encoder = OneHotEncoder(variables=df.columns[df.dtypes == 'object'].to_list(), drop_last=False)
    df_ohe = encoder.fit_transform(df)
    return df_ohe

@st.cache
def calculate_corr_pps(df_ohe):
    """
    Calculates the Spearman and Pearson correlations , and the Predictive Power Score (PPS) matrix.
    """
    df_corr_spearman = df_ohe.corr(method="spearman")
    df_corr_pearson = df_ohe.corr(method="pearson")
    pps_matrix_raw = pps.matrix(df_ohe)
    pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(columns='x', index='y', values='ppscore')
    return df_corr_spearman, df_corr_pearson, pps_matrix

def heatmap_corr(df, threshold, figsize, font_annot):
    """
    Plots a heatmap of the correlation matrix with a given threshold.
    """
    mask = np.zeros_like(df, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    mask[abs(df) < threshold] = True
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(df, annot=True, mask=mask, cmap='viridis', annot_kws={"size": font_annot}, ax=ax, linewidth=0.5)
    plt.ylim(len(df.columns), 0)
    st.pyplot(fig)

def heatmap_pps(df, threshold, figsize, font_annot):
    """
    Plots a heatmap of the Predictive Power Score (PPS) matrix with a given threshold.
    """
    mask = np.zeros_like(df, dtype=np.bool)
    mask[abs(df) < threshold] = True
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(df, annot=True, mask=mask, cmap='rocket_r', annot_kws={"size": font_annot}, linewidth=0.05, linecolor='grey')
    plt.ylim(len(df.columns), 0)
    st.pyplot(fig)

def plot_scatter(df, variables, target='SalePrice'):
    """
    Plots scatter plots for the specified variables against the target variable.
    """
    for var in variables:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=df, x=var, y=target, ax=ax)
        plt.title(f'{var} vs {target}')
        st.pyplot(fig)

def plot_box(df, variables, target='SalePrice'):
    """
    Plots box plots for the specified categorical variables against the target variable.
    """
    for var in variables:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=df, x=var, y=target, ax=ax)
        plt.title(f'{var} vs {target}')
        st.pyplot(fig)

def page_correlation_body():
    """
    Display the correlated features and visualizations on a Streamlit page.
    """
    df3 = load_housing_cleaned()
    df_ohe = preprocess_data(df3)
    df_corr_spearman, df_corr_pearson, pps_matrix = calculate_corr_pps(df_ohe)

    variables_to_study = [
        'GrLivArea', 'YearBuilt', 'GarageArea', 'OpenPorchSF',
        'TotalBsmtSF', '1stFlrSF', 'YearRemodAdd', 'GarageYrBlt',
    ]

    categorical_vars = ['OverallQual', 'KitchenQual_Ex', 'KitchenQual_Gd']

    
    df_eda = df3.filter(variables_to_study + ['SalePrice'])

    # EDA visualizations
    st.header("""Housing prices correlation study""")
    st.info("""
    **BR1:** - The client is interested in knowing how house 
    attributes correlate with sale prices.
    """)
    st.write("""
    A correlation study was conducted to understand how the variables
    are correlated to sale price of a property. The result of the 
    correlation study showed that the most correlated variables
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
    if st.checkbox("Heatmaps: Spearman, Pearson and PPS Correlations", key='heatmaps_1'):
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
        st.subheader("Summary")
        st.write("""
        After correlation heatmaps between variables .corr method was
        used, the return value was a pandas series, and the first items was the
        correlation between SalePrice and SalePrice. Since it was correlation between
        the target variable(SalePrice) itself then [1:] was used to exclude it from
        the series. Next, the remaining values were sorted considering the absolute value,
        which was done by setting key=abs. Then top 11 values were going to be shown.
        Only positive values were taken from both Spearman and Pearson correlations against
        SalePrice. After that they were combined and the result was:
        
        1. OverallQual (0.809829)
        2. GrLivArea (0.731310)
        3. YearBuilt (0.652682)
        4. GarageArea (0.649438)
        5. TotalBsmtSf (0.636999)
        6. 1stFlrSF (0.620743)
        7. YearRemodAdd (0.571159)
        8. GarageYrBlt (0.563256)
        9. KitchenQual_Ex (0.504094)
        10. KitchenQual_Gd (0.478583)
        11. OpenPorchSF (0.477889)
        """)

    if st.checkbox("""Scatter Plots with the most important continous numerical variables
    against the SalePrice""", key='scatter_plots_1'):
        plot_scatter(df_eda, variables_to_study)
        st.subheader("Summary of Insights:")
        st.write("""
        1. Large first-floor areas are associated with higher sale prices.
        2. Larger garage areas generally lead to higher sale prices.
        3. There is clear historical trend showing increased value for more
        recently built garages.
        4. Larger above-ground living areas are associated with higher sale prices.
        5. Slight increase in sale prices with larger open porch areas. Wide spread
        and variability in sale prices for similar porch sizes. Many properties
        with zero open porch area clustering at lower sale prices.
        6. Larger basement areas are associated with higher sale prices. High-value
        properties with extensive basements.
        7. Not surprisingly, houses built more recently generally have higher sale prices.
        Significant increase in sale prices for houses built after 1980, especially after 2000.
        Some older houses have high sale prices, possibly due to renovations or historical value.
        8. More recent remodels and additions are associated with higher sale prices. 
        Notable increase in sale prices for houses remodeled after 2000.
        """)

    if st.checkbox("""Box plots with the most important categorical variables
    against the SalePrice""", key='box_plots_1'):
        plot_box(df_ohe, categorical_vars)
        st.subheader("Box Plot Insights:")
        st.write("""
        1. Kitchen quality:
        * Both excellent and good kitchen quality significantly contribute to higher
        sale prices. However the impact is more substantial for excellent kitchen quality.
        2. Overall quality:
        * Overall quality has a strong positive correlation with sale prices, showing
        that higher overall quality ratings generally lead to higher sale prices.
        3. Market value:
        * Houses with higher kitchen quality and overall quality not only comman higher median
        prices but also show greater variability and a higher propensity for outliers in the 
        upper price range.
        """)

page_correlation_body()



