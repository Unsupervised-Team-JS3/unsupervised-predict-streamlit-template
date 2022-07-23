"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
from email import message
from email.mime import image
from turtle import width
from unicodedata import name
from pyparsing import col
import streamlit as st
from PIL import Image


# Data handling dependencies
import pandas as pd
import numpy as np


# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview","EDA","MODEL","About Us","Contact Us"]
   

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")
    if page_selection == "EDA":
        st.title("Our findings displayed graphically")
        image = Image.open("./resources/imgs/bar.jpeg")
        st.image(image)
        st.caption("Observation from the bar graph of ratings")
        st.markdown("We see half scores (0.5,1.5,2.5,3.5 and 4.5) are less commonly used then integer score values.")
        image = Image.open("./resources/imgs/scatter_plot.png")
        st.image(image)
        st.caption("Examining the data by plotting it in scatter plot")
        st.markdown("""From the graph above we can see there is one outlier which close to 13000 reviews,which is outlier which close
                    to 1300 reviews,which is unlikely""")
        image = Image.open("./resources/imgs/ave_rating.png")
        st.image(image)
        st.caption("Average rating over time")
        st.markdown("""Ïn the chart above we have another anomaly ,the year 1995 has an average of 5.0.This is possibly due to a very small
                sample size or human error""")            
    if page_selection == "MODEL":
        st.title("Models we tried:") 

   
    if page_selection == "About Us":
        st.title("More about the team:")
        st.subheader("Our values")
        st.markdown("-Accountability and Collaboration")
        st.write("-Continuous improvement and Innovative")
        st.write("-Customer commitmentHonesty")
      
        st.subheader("Our Aim")
        st.markdown("We promise steller service,our suppliers a valuable partner,our investors the prospects of sustained profitable growth,and our employees the allure of huge impact")
        st.subheader("Our Vision")
        st.markdown("A possibility is that JS3’s vision statement could include other variables that represent business performance, such as profitability and number of corporate partners. On the other hand, considering the broadness of JS3’s corporate mission statement, business diversification is expectable.The company will add more business ventures to its portfolio, in addition to original content production and on-demand digital content movie recommender that the mission statement encompasses")
        st.subheader("Our Team")
        st.subheader("")
        image = Image.open("./resources/imgs/Theo.jpeg")
        st.image(image,'Theo Sdinani:Co-founder\n', width = 150)
        image = Image.open("./resources/imgs/Menzi.jpeg")
        st.image(image,'Menzi:Web Designer\n',width = 150) 
        col1,col2 = st.columns(2)
        #with col1:
 
        with col1:
            st.subheader("")
            image = Image.open("./resources/imgs/Daniel.jpg")
            st.image(image,'Daniel Komape:Data Analyst\n', width=200)
            image = Image.open("./resources/imgs/Mokgadi.jpg")
            st.image(image,'Mokgadi:Data scientist\n',width=200)
        with col2:
            st.subheader("")
            image = Image.open("./resources/imgs/Success.jpg")
            st.image(image,'Success:Software Developer\n', width=200)
            image = Image.open("./resources/imgs/Njabulo.jpg")
            st.image(image,'Njabulo:UI/UX Designer\n', width=200)                               
                       
    
     # Building out the "Contact Us" page
        st.subheader("")
    if page_selection == "Contact Us":
       
       st.title("JS3 company")
       
       st.header("Message Us")
       with st.form("form",clear_on_submit = True):
        name = st.text_input("Enter full name")
        email = st.text_input("Enter Email Address")
        message = st.text_area("message")
        submit = st.form_submit_button("Submit")
        col1,col2,col3 = st.columns(3)
        with col1:
            st.subheader("Address")
            img = Image.open("./resources/imgs/map.jpg")
            st.image(img)
            st.markdown("1078 Jubert str")
            st.markdown("JHB")
            st.markdown("2023")
            with col2:
                st.subheader("Phone")
                st.markdown("Monday-Friday")
                st.markdown("08h00-17h00 GMT+2")
                st.markdown("(+27) 7895 68974")
                st.markdown("(+27) 9852 25417")
                st.markdown("Holidays")
                st.markdown("08h00-15h00")
                with col3:
                    st.subheader("Email")
                    st.markdown("andersonsmith@gmail.com")
                    st.markdown("leratoM@gmail.com")
       
       #img5 = Image.open("Njabulo.jpg")
       #st.markdown("We the JS3 company we will give you the best recommender")
      

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
