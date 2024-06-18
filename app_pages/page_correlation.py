import streamlit as st

def page_correlation_body():
    """
    Display the correlated features.
    """
    df3 = load_housing_cleaned()
    
    variables_to_study = ['OverallQual', 'GrLivArea', 'YearBuilt', 'GarageArea', 'TotalBsmtSF', 
                        '1stFlrSF', 'YearRemodAdd', 'GarageYrBlt', 'KitchenQual', 'OpenPorchSF']

    st.title("""Housing prices correlation study""")
    st.info("""
    **BR1:** - The client is interested in knowing how house 
    attributes correlate with sale prices.
    """)
    st.write("""
    A correlation study was conducted to understand how the variables
    are correlated to sale price of a property. With the result the first business
    requirement was addressed.
    The result of the correlation study showed that the most correlated variables
    to the Sale Price are:
    {variables_to_study}
    """)

