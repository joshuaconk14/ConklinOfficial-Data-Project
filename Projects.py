import streamlit as st
import pandas as pd



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
    with st.container():
        image_url = "pictures/Bravo_company_pic_copy.png"
        col1, col2 = st.columns([1,2])
        with col1:
            st.image(image_url, width = 250)
        with col2:
            st.subheader("BravoTekk - Mobile App Front-End Development")
            st.write("(App currently being built)")
            streamlit_url = "https://github.com/joshuaconk14/Tekk_UI_Project.git"
            st.markdown(f"[Visit Github Repo]({streamlit_url})")
    st.write("September 2024 - Present")
    st.write("Use Xcode, SwiftUI, and Rive to build app interface for sports training mobile application.")
    st.write("")
    st.write("Skills: SwiftUI, Xcode, Rive, User Expereince (UX), User Interface Design, Software Design, Animation")
    st.write("##")
    st.write("##")

    #Project 2
    with st.container():
        image_url = "pictures/datajob_ss1.png"
        col1, col2 = st.columns([1,2])
        with col1:
            st.image(image_url, width = 250)
        with col2:
            st.subheader("Programming Language Mentions Analysis - Mentions from Data Jobs")
            # create pdf button
            with open("files/Data_Jobs_Tableau_Story_copy.pdf","rb") as pdf_file:
                pdf_story = pdf_file.read()
            st.download_button("View Full Project Display", data = pdf_story, file_name = "files/Data_Jobs_Tableau_Story_copy.pdf")
            #with st.expander("Programming Language Mentions Analysis - Mentions from Data Jobs"):
                #image_url = "pictures/datajob_ss1.png"
                #st.image(image_url, width = 900)
                #image_url = "pictures/datajob_ss2.png"
                #st.image(image_url, width = 900)
            streamlit_url = "https://github.com/joshuaconk14/Data_Jobs_Project.git"
            st.markdown(f"[Visit Github Repo]({streamlit_url})")
    st.write("August 2024 - September 2024")
    st.write("Used SQL and Tableau in order to determine which programming languages were mentioned the most in job descriptions for data roles. Helps data job seekers know what languages they need to practice for specific data jobs.")
    st.write("")
    st.write("Skills: SQL, Tableau, Azure Studio, Databases, Storytelling, Data Visualization, Big Data, Data Connection, Performance Optimization")
    st.write("##")
    st.write("##")
    

    #Project 3
    with st.container():
        image_url = "pictures/COproj_ss.png"
        col1, col2 = st.columns([1,2])
        with col1:
            st.image(image_url, width = 250)
        with col2:
            st.subheader("ConklinOfficial KPIs Dashboard")
            st.markdown("[View Full Project Display](https://co-kpis-project.streamlit.app/)")
            streamlit_url = "https://github.com/joshuaconk14/CO_KPIs_Project.git"
            st.markdown(f"[Visit Github Repo]({streamlit_url})")
    st.write("Jul 2024 - Aug 2024")
    st.write("Extracted KPI data from ConklinOfficial Instagram page into Python, creating data story correlating the relationship between KPIs and the type of content posted.")
    st.write("")
    st.write("Skills: Python, Jupyter, Pandas, Numpy, HTML, Data Extraction, Data Visualization, Software Design, Data Analysis")
    st.write("##")
    st.write("##")

# Project 4
    with st.container():
        image_url = "pictures/Qualtrics_ss.png"
        col1, col2 = st.columns([1,2])
        with col1:
            st.image(image_url, width = 250)
        with col2:
            st.subheader("Qualtrics Survey - Marketing Analytics")
            st.markdown(f"[View Full Project Display](https://sjsu.qualtrics.com/jfe/form/SV_2gwvgq9OUSAKoF8)")
            streamlit_url = "https://github.com/joshuaconk14/Qualtrics_Survey_Project.git"
            st.markdown(f"[Visit Github Repo]({streamlit_url})")
    st.write("Feb 2024 - May 2024")
    st.write("Used Rstudio to create and conduct a survey through Qualtrics. Data analysis on people's opinions on influencer marketing affecting consumer purchasing behavior.")
    st.write("")
    st.write("Skills: R, Excel, Data Analysis, Research Design, Qualitative Research, Business Analytics, Microsoft Excel, Data Entry")
    st.write("##")
    st.write("##")

# Project 4
    with st.container():
        image_url = "pictures/FYSC_logo.png"
        col1, col2 = st.columns([1,2])
        with col1:
            st.image(image_url, width = 150)
        with col2:
            st.subheader("Logo - Fremont Youth Soccer Club")
            streamlit_url = "https://www.fremontyouthsoccer.com/2017/02/the-new-fremont-youth-soccer-club-badge/"
            st.markdown(f"[View Project Announcement]({streamlit_url})")
    st.write("Jan 2017 - Feb 2017")
    st.write("Created FYSC official logo that is being used today. Creatively incorporated club values onto the logo using Adobe Illustrator.")
    st.write("")
    st.write("Skills: Adobe Illustrator, Graphic Design, Creativity Skills")