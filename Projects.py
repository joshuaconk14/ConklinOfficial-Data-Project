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
    st.write("August 2024")
    st.write("Used SQL and Tableau in order to determine which programming languages were mentioned the most in job descriptions for data roles (mainly Data Engineers, Data Analysts, and Data Scientists). This is to help data job seekers know what programming languages they need to understand and practice for specific data jobs.")
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
            st.subheader("ConklinOfficial KPI Dashboard - Relationship between KPIs and Content")
            st.markdown("[View Full Project Display](https://co-kpis-project.streamlit.app/)")
            streamlit_url = "https://github.com/joshuaconk14/CO_KPIs_Project.git"
            st.markdown(f"[Visit Github Repo]({streamlit_url})")
    st.write("Jul 2024 - Aug 2024")
    st.write("Used Python, Pandas, and Numpy demonstrate the relationship between KPIs and the type of reel posted, indicating what type of post performs best and which posts posts we should focus on.")
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
    st.write("Conducted a survey through Qualtrics platform, create with Rstudio, to research people's opinions on influencer marketing affecting consumer purchasing behavior. Coded the data and analyze the participant response trends in order to make future predictions.")
    st.write("")
    st.write("Skills: R, Excel, Data Analysis, Research Design, Qualitative Research, Business Analytics, Data Entry")
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
    st.write("Created FYSC official logo with Adobe Illustrator that is being used today. Creatively incorporated club values and worked with board members presenting multiple ideas to create the best logo possible.")
    st.write("")
    st.write("Skills: Adobe Illustrator, Graphic Design, Creativity Skills")