import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def app():
    # title
    title_html = """
    <h1 style = "text-align: center; color: gray; padding: 50px">Projects</h1>
    """
    st.markdown(title_html, unsafe_allow_html = True)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    # ?? expander hover color-changer doesn't work
    #st.markdown(
        #"""
        #<style>
        #.stExpander:hover .stExpanderHeader {
            #color: blue !important;
        #}
        #</style>
        #""",
        #unsafe_allow_html = True
    #)

    #Project 1
    with st.expander("Programming Language Mentions Analysis - Mentions from Data Jobs"):
        image_url = "pictures/datajob_ss1.png"
        st.image(image_url, width = 900)
        image_url = "pictures/datajob_ss2.png"
        st.image(image_url, width = 900)
    st.write("August 2024")
    st.write("Used SQL and Tableau in order to determine which programming languages were mentioned the most in job descriptions for data roles (mainly Data Engineers, Data Analysts, and Data Scientists). This is to help data job seekers know what programming languages they need to understand and practice for specific data jobs.")
    st.write("")
    st.write("Skills: SQL, Tableau, Azure Studio, Databases, Storytelling, Data Visualization, Big Data, Data Connection, Performance Optimization")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    

    #Project 2
    with st.expander("ConklinOfficial KPI Dashboard - Relationship between KPIs and Content"):
        streamlit_url = "https://co-kpis-project.streamlit.app/"
        st.markdown(f"({streamlit_url})")
    st.write("Jul 2024 - Aug 2024")
    st.write("Used Python, Pandas, and Numpy demonstrate the relationship between KPIs and the type of reel posted, indicating what type of post performs best and which posts posts we should focus on.")
    st.write("")
    st.write("Skills: Python, Jupyter, Pandas, Numpy, HTML, Data Extraction, Data Visualization, Software Design, Data Analysis")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

# Project 3
    with st.expander("Qualtrics Survey - Marketing Analytics"):
        st.write("https://sjsu.qualtrics.com/jfe/form/SV_2gwvgq9OUSAKoF8")
    st.write("Feb 2024 - May 2024")
    st.write("Conducted a survey through Qualtrics platform, create with Rstudio, to research people's opinions on influencer marketing affecting consumer purchasing behavior. Coded the data and analyze the participant response trends in order to make future predictions.")
    st.write("")
    st.write("Skills: R, Excel, Data Analysis, Research Design, Qualitative Research, Business Analytics, Data Entry")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

# Project 4
    with st.expander("Logo - Fremont Youth Soccer Club"):
        image_url = "pictures/FYSC_logo.png"
        st.image(image_url, width = 300)
        st.write("https://www.fremontyouthsoccer.com/2017/02/the-new-fremont-youth-soccer-club-badge/")
    st.write("Jan 2017 - Feb 2017")
    st.write("Created FYSC official logo with Adobe Illustrator that is being used today. Creatively incorporated club values and worked with board members presenting multiple ideas to create the best logo possible.")
    st.write("")
    st.write("Skills: Adobe Illustrator, Graphic Design, Creativity Skills")