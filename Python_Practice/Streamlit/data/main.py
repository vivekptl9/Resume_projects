import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

#? Set Page Configuration
st.set_page_config(page_title="Data Visualizer",
                layout="centered",
                page_icon="📊")

#? Title

st.title("📊 Data Visualizer - Web App" )

#? Getting the working directory
working_dir = os.path.dirname(os.path.abspath(__file__))
#print(f"Working Directory: {working_dir}")

#? Folder path
folder_path = f"{working_dir}"
#print(f"Folder Path: {folder_path}")

#? List of files
files_list = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

#? Dropdown for all the files
selected_file = st.selectbox("Select a file", files_list, index=None)


if selected_file:
    file_path = os.path.join(folder_path,selected_file)
    print(file_path)
    
    df = pd.read_csv(file_path)
    
    col1,col2 = st.columns(2)    
    columns = df.columns.tolist()
    
    with col1:
        st.write("")
        st.write(df.head())
    with col2:
        x_axis = st.selectbox("Select the X-axis", options=columns+["None"], index=None)
        y_axis = st.selectbox("Select the Y-axis", options=columns+["None"], index=None)
        plot_list = ["Line Plot", "Bar Chart", "Scater Plot", "Distribution Plot", "Count Plot"]
        
        selected_plot = st.selectbox("Selected a Plot", options=plot_list, index=None)
        
        st.write(x_axis)
        st.write(y_axis)
        st.write(selected_plot)
        

    



