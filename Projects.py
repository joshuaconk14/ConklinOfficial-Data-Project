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
    
    with st.expander("ConklinOfficial KPI Dashboard - Relationship between KPIs and Content"):
        # Project title
        title_html = """
        <h1 style = "text-align: center; color: gray; padding: 20px; font-size: 1.8em;">ConklinOfficial KPI Dashboard - Analyzing Relationship between KPIs and Content</h1>
        """
        st.markdown(title_html, unsafe_allow_html = True)

        # read file
        st.write("### Raw data")
        df = pd.read_csv(r"data/CO_Post_Multi_Data_3_months.csv")
        # hide Account ID column
        # columns_to_hide = ["Account ID"]
        # df_visible = df.drop(columns=columns_to_hide)
        st.write(df)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")


        # Convert to datetime
        df['Publish time'] = pd.to_datetime(df['Publish time'])

        # Put publish time in alphabetical order
        df = df.sort_values(by='Publish time')

        # Get rid of time posted in x-axis
        df['Publish time'] = df['Publish time'].astype(str).apply(lambda x: x.split()[0] if isinstance(x, str) else x)



        # Streamlit app
        st.write("### Likes on Posts in the Last 3 Months")

        # interactive chart
        fig = px.bar(df, x='Publish time', y='Likes', labels={'Publish time': 'Publish time', 'Likes': 'Likes'})
        
        fig.update_traces(
            hovertemplate=f'<b>Publish Time:</b> %{{x}}<br><b>Likes:</b> %{{y}}<extra></extra>'
        )

        # Create performance lines for custom y-axis graph
        q80 = np.percentile(df['Likes'], q=80)
        q20 = np.percentile(df['Likes'], q=20)


        # Create performance lines for custom y-axis graph
        fig.add_shape(
            type='line', x0=df['Publish time'].min(), y0=q80, x1=df['Publish time'].max(), y1=q80,
            line=dict(color='green', dash='dash'), name = 'Good Performance (80th percentile)'
        )
        fig.add_shape(
            type='line',x0=df['Publish time'].min(), y0=q20, x1=df['Publish time'].max(),y1=q20,
            line=dict(color='red',dash='dash'), name= 'Bad Performance (20th percentile)'
        )

        # rest of info for legend and grid
        fig.update_layout(
            showlegend=True,
            xaxis_title='Publish time',
            yaxis_title='Likes',
            xaxis=dict(showgrid=True, tickangle=0),
            yaxis=dict(showgrid=True)
        )

        # Display the plot for 'Likes on Posts in the Last 3 Months' in streamlit
        st.plotly_chart(fig)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")











        # Allow user to click permalink based off of the amount of likes it has
        st.write("### Click on a date to open the corresponding Instagram post")
        for i, row in df.iterrows():
            st.write(f"[{row['Publish time']}]({row['Permalink']}) - {row['Likes']} likes")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")









        # Add Streamlit widget for user to select different y-axis (KPI) data
        st.write("### Click on the drop-down menu to choose which KPI metric you would like to observe")
        allowed_columns = ['Saves', 'Shares', 'Reach', 'Plays', 'Likes', 'Impressions', 'Follows', 'Comments']
        allowed_columns.sort()
        y_axis = st.selectbox("Select Y-axis",allowed_columns)

        # interactive chart
        fig = px.bar(df, x='Publish time', y=y_axis, labels={'Publish time': 'Publish time', y_axis: y_axis})
        fig.update_traces(
            hovertemplate=f'<b>Publish Time:</b> %{{x}}<br><b>{y_axis}:</b> %{{y}}<extra></extra>'
        )

        # Create performance lines for custom y-axis graph
        q80 = np.percentile(df[y_axis], q=80)
        q20 = np.percentile(df[y_axis], q=20)


        # Create performance lines for custom y-axis graph
        fig.add_shape(
            type='line', x0=df['Publish time'].min(), y0=q80, x1=df['Publish time'].max(), y1=q80,
            line=dict(color='green', dash='dash'), name = 'Good Performance (80th percentile)'
        )
        fig.add_shape(
            type='line',x0=df['Publish time'].min(), y0=q20, x1=df['Publish time'].max(),y1=q20,
            line=dict(color='red',dash='dash'), name= 'Bad Performance (20th percentile)'
        )

        # rest of info for legend and grid
        fig.update_layout(
            showlegend=True,
            xaxis_title='Publish time',
            yaxis_title= y_axis,
            xaxis=dict(showgrid=True, tickangle=0),
            yaxis=dict(showgrid=True)
        )


        # Display the updated plot in Streamlit
        st.plotly_chart(fig)
        st.write("")
        st.write("")
        st.write("")
        

        # results
        st.write("### Analysis")
        st.write("")
        st.write("Over the past three months, ConklinOfficial has provided a variety of soccer content, mainly sharing how-to's, ball mastery drills, coaching tips, mentality advice, and habit improvements. Key performance indicators such as likes, comments, shares, and reach have allowed us to figure out which type of posts are performing best. We will use likes, saves, and shares as our main KPIs for this analysis. Data below the red Bad Performance line are posts that haven't performed well, and data above the green Good Performance line are posts that have performed well and have matched our goal for that KPI. Posts lying in between the lines have performed decently.")
        st.write("")
        st.write("Habit improvement videos have good engagement from our audience, with posts from April 28, May 14, and May 30 hitting 1,897, then 545, and then 400 likes respectively and comfortably above the Bad performance line. Mentality advice videos have not performed well, with posts from May 21 and May 28 hovering closer to the Bad Performace line with 206 and 354 likes. How-to videos have shown to be clear favorites, with posts on May 26 and May 27 getting 18,542 and 14,233 likes respectively. They also have far more saves and shares than other post types, with 2,974 and 4,986 saves, and 1,800 and 2,157 shares respectively.")
        st.write("")
        st.write("")
        st.write("### Strategic Planning")
        st.write("")
        st.write("Based on the results, how-to videos have been the best performing videos in the past three months, and are the preferred videos by our audience members. Our goal will be to increase the ratio of how-to videos to other content by 20%, mainly being striking tutorials since the two how-to videos were 'rabona' and 'power shot' tips.")
    
    # Project 1 description
    st.write("Jul 2024 - Aug 2024")
    st.write("Data Engineering and Analytics project demonstrating the relationship between KPIs and the type of reel posted, indicating what type of post performs best and which posts posts we should focus on.")
    st.write("")
    st.write("Skills: Python, Jupyter, Pandas, Numpy, HTML, Data Extraction, Software Design, Data Analysis, Data Analytics")
    st.write("")
    st.write("")
    st.write("")
    st.write("")


    with st.expander("Qualtrics Survey - Marketing Analytics"):
        st.write("https://sjsu.qualtrics.com/jfe/form/SV_2gwvgq9OUSAKoF8")
    st.write("Feb 2024 - May 2024")
    st.write("Conducted a survey through Qualtrics platform to research people's opinions on influencer marketing affecting consumer purchasing behavior. Used Rstudio to code the data and analyze the participant response trends in order to make future predictions.")
    st.write("")
    st.write("Skills: R, Excel, Data Analysis, Research Design, Qualitative Research, Business Analytics, Data Entry")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    with st.expander("Logo - Fremont Youth Soccer Club"):
        image_url = "pictures/FYSC_logo.png"
        st.image(image_url, width = 300)
        st.write("https://www.fremontyouthsoccer.com/2017/02/the-new-fremont-youth-soccer-club-badge/")
    st.write("Jan 2017 - Feb 2017")
    st.write("Created FYSC official logo that is being used today. Creatively incorporated club values onto the logo using Adobe Illustrator.")
    st.write("")
    st.write("Skills: Adobe Illustrator, Graphic Design, Creativity Skills")