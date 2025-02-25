# import streamlit as st
# import pandas as pd 
# import os
# from io import BytesIO

# st.set_page_config(page_title="Data Sweeper", layout="wide")

# #Custom CSS
# st.markdown(
#     """"
#     <style>
#     .stAPP
#     {
#     background-color: black;
#     color: white;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# #Title and description
# st.title("Datasweeper Sterling Integrator By DH Daniyaal")
# st.write("Transform your file between CSV abd Excel format with built-in data cleaning and visulization Creating the project for quarter 3!")

# #Uploader files
# uploaded_files = st.file_uploader("Upload your files (Accept CSV or Excel):", type=["csv, xlsx"], accept_multiple_files=(True))

# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()

#         if file_ext == ".csv":
#             df = pd.read_csv(file)
#         elif file_ext == "xlsx":
#             df = pd.read_excel(file)
#         else:
#             st.error(f"Unspotted file type: {file_ext}")
#             continue

# #File details
# st.write("Preview the head of the Dataframe")
# st.dataframe(df.head())

# #Data cleaning options
# st.subheader("Data cleaning options")
# if st.checkbox(f"Clean data for {file.name}"):
# col1, col2 = st.columns(2)

# with col1:
#     if st.button(f"Remove duplicates from the file: {file.name}"):
#         df.drop_duplicates(inplace=True)
#         st.write("Duplicates remove!")

# with col2:
#     if st.button(f"File missing values for {file.name}"):
#         numeric_cols = df.select_dtypes(include=['number']).columns
#         df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#         st.write("Missing values have been filled!")


