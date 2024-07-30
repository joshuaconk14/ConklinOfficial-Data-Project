import streamlit as st

def app():
    # title
    title_html = """
        <h1 style = "text-align: center; color: gray; padding: 10px">Home</h1>
        <h2 style = "text-align: center; color: gray; padding: 0px"> -- </h2>
        <h3 style = "text-align: center; color: gray; padding: 10px">Joshua Conklin Projects</h3>
        """
    st.markdown(title_html, unsafe_allow_html = True)

    # intro
    st.write("")
    st.write("")
    st.write("Welcome to my website where I display my projects using Python to extract data from the web, design graphic displays, and analyze key metrics to make strategic business decisions! I also created this website with Streamlit, using Python and stylesheet languages (HTML and CSS) in VS Code.")
    st.write("")
    st.write("")
    st.write("I am a fourth year student at the Lucas College and Graduate School of Business, stepping closer towards my bachelor's degree in Business Administration/ Marketing, with a growing interest in business analytics and data science. I have played for the Ohlone College Men's Soccer Team and the San Jose State Men's Club Soccer Team during my time in college. As an avid soccer player and former soccer-coach, I have a passion for applying my creativity and knowledge to the world around me. Although I am a marketing major, I would love to explore a multitude of data roles, such as data science and management. I look forward to what the future has in store for me, and to continuously grow in my pursuit for accomplishment.")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    # image upload
    image_url = "/Users/Joshua/Desktop/venv/CO_streamlit_app/pictures/profpic1.jpg"
    st.image(image_url, use_column_width = True)
