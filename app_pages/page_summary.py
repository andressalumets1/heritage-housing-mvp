import streamlit as st

def page_summary_body():

    st.header("""Project Summary""")
    st.subheader("""Introduction""")
    st.write("""
    Welcome to the Heritage Housing Issues project. This initiative is centered
    around aiding our client in understanding how various attributes influence sale prices
    in Ames, Iowa. the client has inherited four houses and seeks not only to
    comprehend the factors impacting their market value but also to predict their
    sale prices accurately. Additionally, the client desires the ability to predict
    the sale price of any other house within the Ames area.
    """)


    st.subheader("""Dataset Content""")
    st.write("""
    * The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
    * The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

    |Variable|Meaning|Units|
    |:----|:----|:----|
    |1stFlrSF|First Floor square feet|334 - 4692|
    |2ndFlrSF|Second-floor square feet|0 - 2065|
    |BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
    |BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
    |BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
    |BsmtFinSF1|Type 1 finished square feet|0 - 5644|
    |BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
    |TotalBsmtSF|Total square feet of basement area|0 - 6110|
    |GarageArea|Size of garage in square feet|0 - 1418|
    |GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
    |GarageYrBlt|Year garage was built|1900 - 2010|
    |GrLivArea|Above grade (ground) living area square feet|334 - 5642|
    |KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
    |LotArea| Lot size in square feet|1300 - 215245|
    |LotFrontage| Linear feet of street connected to property|21 - 313|
    |MasVnrArea|Masonry veneer area in square feet|0 - 1600|
    |EnclosedPorch|Enclosed porch area in square feet|0 - 286|
    |OpenPorchSF|Open porch area in square feet|0 - 547|
    |OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
    |OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
    |WoodDeckSF|Wood deck area in square feet|0 - 736|
    |YearBuilt|Original construction date|1872 - 2010|
    |YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
    |SalePrice|Sale Price|34900 - 755000|
    """)

    st.subheader("""Business Requirements:""")
    st.write("""
    The project has two business requirements:

    **BR1:** - The client is interested in discovering how house attributes correlate
    with sale prices.

    **BR2:** - The client is interested in predicting the house sale prices from 4 houses,
    that she inherited and any other house in Ames, Iowa.
    """)

    st.subheader("""README""")
    st.write("""
    For additional information, please visit and read the
    [Project README file](https://github.com/andressalumets1/heritage-housing-mvp.git).
    """)