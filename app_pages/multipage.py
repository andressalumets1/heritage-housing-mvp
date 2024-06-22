import streamlit as st
import logging

logging.basicConfig(level=logging.DEBUG)

# Class to generate multiple Streamlit pages using an object oriented approach
class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

    def add_page(self, title, func) -> None:
        logging.debug(f"Adding page: {title}")
        self.pages.append({"title": title, "function": func })

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio("Menu", self.pages, format_func=lambda page: page['title'])
        logging.debug(f"Selected page: {page['title']}")
        try:
            page['function']()
        except Exception as e:
            logging.exception("Exception occured while running the page function")
            st.error(f"An error occurred: {e}")