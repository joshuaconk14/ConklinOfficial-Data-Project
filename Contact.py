import streamlit as st


def app():
    # title
    title_html = """
        <h1 style = "text-align: center; color: gray; padding: 50px">Contact</h1>
        """
    st. markdown(title_html, unsafe_allow_html = True)


    st.write("")
    st.subheader("""
    LinkedIn
    https://www.linkedin.com/in/joshua-conklin/
    """)
    st.write("###")
    st.subheader("""
    GitHub
    https://github.com/joshuaconk14/Josh-Conk-Project-Portfolio.git
    """)
    st.write("###")
    st.subheader("""
    Instagram
    """)
    username = ["joshuaconk"]
    for user in username:
        profile_url = f"https://www.instagram.com/{user}/"
    st.markdown(f"@[{user}]({profile_url})")
    st.write("###")
    st.subheader("""
    Email
    joshua@caffeinated.org
    """)
