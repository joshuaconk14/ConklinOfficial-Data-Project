import streamlit as st


def app():
    # title
    title_html = """
        <h1 style = "text-align: center; color: gray; padding: 50px">Contact</h1>
        """
    st. markdown(title_html, unsafe_allow_html = True)

    # contact info
    st.write("Welcome to my contacts list, here you can find ways to contact me.")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("LinkedIn: \n\nhttps://www.linkedin.com/in/joshua-conklin/")
    st.write("")
    st.write("")
    st.write("Github: \n\nhttps://github.com/joshuaconk14/COProject.git")
    st.write("")
    st.write("")
    st.write("Instagram:")
    username = ["joshuaconk"]
    for user in username:
        profile_url = f"https://www.instagram.com/{user}/"
        st.markdown(f"@[{user}]({profile_url})")
    st.write("")
    st.write("")
    st.write("email: \n\njoshua@caffeinated.org")