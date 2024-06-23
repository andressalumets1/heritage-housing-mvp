import streamlit as st
import logging

logging.basicConfig(level=logging.DEBUG)

# Class to generate multiple Streamlit pages using an object oriented approach
class MultiPage:

    def __init__(self, app_name) -> None:
        """
        Initializes the MultiPage class.

        Parameters:
        - app_name (str): The name of the application.

        Attributes:
        - pages (list): An empty list to store the pages of the app.
        - app_name (str): Stores the name of the application.
        """
        self.pages = []
        self.app_name = app_name

    def add_page(self, title, func) -> None:
        """
        Adds a new page to the app.
        This method appends a dictionary with the page title and function to the pages list.
        A debug log message is generated indicating that a page is being added.
        """
        logging.debug(f"Adding page: {title}")
        self.pages.append({"title": title, "function": func })

    def run(self):
        """
        Runs the app, displaying the title and a sidebar menu for navigation.
        
        The method sets the app title, creates a radio button menu in the sidebar
        for selecting pages, and executes the function of the selected page.
        If an exception occures while running the page function, it is caught, logged,
        and an error message is displayed to the user.
        """
        st.title(self.app_name)
        page = st.sidebar.radio("Menu", self.pages, format_func=lambda page: page['title'])
        logging.debug(f"Selected page: {page['title']}")
        try:
            page['function']()
        except Exception as e:
            logging.exception("Exception occured while running the page function")
            st.error(f"An error occurred: {e}")