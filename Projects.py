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

    # intro
    st.write("Hello, here is my ConklinOfficial Data Engineering and Analytics project demonstrating the relationship between KPIs and the type of reel posted, indicating what type of post performs best and which posts posts we should focus on.")
    st.write("")
    st.write("")
    st.write("This is currently my only project as of now, more coming soon.")
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
    #with st.expander("ConklinOfficial KPI Analysis - Relationship between KPIs and Content"):

    # Project title
    title_html = """
    <h1 style = "text-align: center; color: gray; padding: 20px; font-size: 1.8em;">ConklinOfficial KPI Analysis - Relationship between KPIs and Content</h1>
    """
    st.markdown(title_html, unsafe_allow_html = True)

    # read file
    st.write("### Raw data")
    df = pd.read_csv(r"/Users/Joshua/Desktop/My_projects/CO_proj_data/CO_Post_multi_data_3_months.csv")
    # hide Account ID column
    columns_to_hide = ["Account ID"]
    df_visible = df.drop(columns=columns_to_hide)
    st.write(df_visible)
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