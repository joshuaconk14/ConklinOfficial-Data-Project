import streamlit as st
#these two imports were used for making pic into circle
from PIL import Image, ImageDraw
from IPython.display import display, HTML

def app():
    # title
    title_html = """
        <h1 style = "text-align: center; color: gray; padding: 10px">Home</h1>
        <h2 style = "text-align: center; color: gray; padding: 0px"> -- </h2>
        <h3 style = "text-align: center; color: gray; padding: 10px">Joshua Conklin Project Portfolio</h3>
        """
    st.markdown(title_html, unsafe_allow_html = True)


    # image upload and centering
    st.write("")
    st.write("")
    image_url = "pictures/circular_image.png"
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(image_url, width=500)

    # intro
    st.write("")
    st.write("")
    st.write("Welcome to my website where I display my projects using programming languages such as Python, SQL, and R to extract data from the web, design interactive graphs, and analyze key metrics to make strategic business decisions! I also created this website with Streamlit, using Python, Pandas, NumPy, and HTML in VS Code.")
    st.write("")
    st.write("---")



    #experience and education summarization
    with st.container():
        col4, col5 = st.columns(2)
        with col4:
            st.subheader("""
            Experience
            - Data Engineering - ConklinOfficial
                - 2024 - Present
            - Marketing Designer - FYSC
                - 2017 - 2022
            - Soccer Coach - FYSC
                - 2022 - 2024
            - Courtesy Clerk
                - 2020 - 2021
        """)
        with col5:
            st.subheader("""
            Education
            - San Jose State University
                - Bachelors Degree in Business Admin/ Marketing
                - Grade: 3.6
            - Ohlone College
                - Associates Degree In Business Administration
                - Grade: 3.8
        """)