#Streamlit
import streamlit as st

st.set_page_config(page_title="growth mindset project", page_icon="★")
st.title("Growth Mindset Challange: Web App With Streamlit")
st.header("Welcome to Your Growth Journey!!")
st.write("⭐ **Streamlit** is an **open-source Python framework** for quickly building **data science and machine learning applications** with minimal coding, without needing complex backend or frontend development. 🚀")

#quote sction
st.header("Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal, it is the courage to countinue thats counds.-Winston churchill")

st.header("What's Your Challange Today?")
user_input = st.text_input("Describe a challange your facing:")

#condition
if user_input:
    st.success(f"You're facing: {user_input}. keep pushing forword towords your goal!")
else:
    st.warning("Tell us about your challange to get started!")

#reflexing
st.header("Reflected Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f" Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on post experience help you grow! share your difficulties")

#acheivments
st.header("Celebrate Your Wins!")
acheivment = st.text_input("Share something you're recently accomplished:")

if acheivment:
    st.success(f"AMazing your acheive: {acheivment}")
else:
    st.info("Big or small, every acheivment counts! share on now!")

#footer
st.write("- - - - -")
st.write("Keep believing in yourself. Growth is a jouney, not a destination!")
st.write("**Created by DaniYaal**")
