
import streamlit as st
from streamlit_option_menu import option_menu
import Home, Projects, Contact




# page configuration on browser
st.set_page_config(
    page_title = "Joshua Conklin Project Portfolio",
    page_icon = "📊",
    layout = "wide",
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