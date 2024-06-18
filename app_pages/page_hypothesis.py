import streamlit as st

def page_hypothesis_body():
    st.header("Project Hypotheses and Validation")
    
    st.subheader("**H1 - Hypothesis 1: Quality of Interior Features and Sale Price**")
    
    st.write("""
    **Null Hypothesis (H₀):** The quality of interior features 
    (e.g., kitchen quality, overall material and finish) 
    does not significantly impact the sale price of houses in Ames, Iowa.

    **Alternative Hypothesis (H₁):**
    Houses with higher-quality interior features command higher 
    sale prices in Ames, Iowa.

    **Rationale:**
    This hypothesis examines whether aspects such as the condition 
    of the kitchen, the quality of materials used throughout the house, 
    and the overall finish of interior spaces correlate with 
    higher sale prices. These features are often significant factors 
    in buyer decisions.
    
    **Findings from the Notebook:**
    * The analysis identified variables such as OverallQual (Overall Quality)
    and KitchenQual (Kitchen Quality) as strongly correlated with higher sale prices.
    * Specifically, houses with excellent kitchen quality (KitchenQual_Ex) and higher
    overall quality (OverallQuality) tend to command higher sale prices.

    **Conclusion:**
    * The findings support Hypothesis 1. There is evidence that the quality of
    interior features, particularly kitchen quality and overall quality, correlates
    positively with sale prices in Ames, Iowa.
    """)



    st.subheader("""**H2 - Hypothesis 2:
    Size and Functional Space Utilization Impact on Sale Price**""")

    st.write("""
    Null Hypothesis (H₀): The size and functional space utilization
    of a house do not significantly affect its sale price in Ames, Iowa.

    Alternative Hypothesis (H₁): Larger houses with efficiently utilized 
    functional space tend to have higher sale prices in Ames, Iowa.

    Rationale: This hypothesis explores whether the physical size of a 
    house and how well its functional spaces are utilized influence its market value. 
    Buyers often prioritize ample living space and well-designed functional areas.
    
    **Findings from the Notebook:**
    * Variables such as GrLivArea (Above Ground Living Area), GarageArea,
    TotalBsmtSF (Total Basement Area), and 1stFlrSF (First Floor Area) were identified
    as influential factors positively correlated with sale prices.
    * Larger sizes in these functional spaces generally lead to higher sale prices.

    **Conclusion:**
    * The analysis supports Hypothesis 2. Larger sizes in functional spaces like
    living area, garage, basement, and first floor correlate positively with higher
    sale prices in Ames, Iowa.
    """)

    st.subheader("Additional Insights:")
    st.write("""
    * The scatter plots and box plots provided visual confirmation of these relationships,
    showcasing how these variables impact sale prices.
    * The use of Pearson and Spearman correlations, as well as Predictive Power Score
    (PPS), helped in quantifying these relationships and identifying the most influential features.
    """)

    st.subheader("Final Assessment:")
    st.write("""
    Both of the hypotheses were effectively answered by providing comprehensive data
    exploration, correlation analysis, and visualizations that clearly demonstrate how
    specific house attributes relate to sale prices in Ames, Iowa. The insights gained from
    this analysis can guide further feature engineering and modeling efforts in predicting house
    sale prices accurately.
    """)
