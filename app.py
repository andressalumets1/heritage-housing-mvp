import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page_summary import page_summary_body
from app_pages.page_correlation import page_correlation_body
from app_pages.page_hypothesis import page_hypothesis_body
from app_pages.page_performance import page_performance_body
from app_pages.page_predict import page_predict_body

app = MultiPage(app_name= "Heritage-housing-MVP")

# App pages here using .add_page()

app.add_page("Project Summary", page_summary_body)
app.add_page("Correlation Study", page_correlation_body)
app.add_page("Hypothesis Study", page_hypothesis_body)
app.add_page("Performance Study", page_performance_body)
app.add_page("Predict Sale Price", page_predict_body)

app.run()

