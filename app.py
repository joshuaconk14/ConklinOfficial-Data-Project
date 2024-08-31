
import streamlit as st
from streamlit_option_menu import option_menu
import Home, Projects, Contact


#import env
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#access secrets
secret_key = st.secrets.get("SECRET_KEY", os.getenv("SECRET_KEY"))
database_url = st.secrets.get("DATABASE_URL", os.getenv("DATABASE_URL"))


# Example usage of secret key and database URL
# st.write(f"Secret Key: {secret_key}")
# st.write(f"Database URL: {database_url}")











# page configuration on browser
st.set_page_config(
    page_title = "Joshua Conklin Projects",
    page_icon = "📊",
    layout = "centered",
    initial_sidebar_state = "auto"
)

# ?? need this?
class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

# create sidebar menu (?? blue hover function doesn't work)
def run():
    with st.sidebar:
        app = option_menu(
            menu_title='Contents',
            options=['Home', 'Projects', 'Contact'],
            icons= ['house-fill','trophy-fill','person-circle'],
            menu_icon='chat-text-fill',
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color":'black',"icon": {"color": "white", "font-size": "23px"},
                            "nav-link":{"color": "white", "font-size": "20px", "text-align": "left", "--hover-color": "02ab21", "margin":"0px" },
                            "nav-link-selected": {"background-color": "02ab21"},}

            }
        )

    if app == 'Home':
        Home.app()
    elif app == 'Projects':
        Projects.app()
    elif app == 'Contact':
        Contact.app()

        
run()



# sidebar color changer?
# 3 columns on project
# get the legend to work
# change url name


# DONE: interactive chart, be able to to see # of likes and the percentile
#(completed, BUT figure out how you did this . it was the %{{x}} thing)   