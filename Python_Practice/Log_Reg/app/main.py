import streamlit as st
import pickle as pickle
import pandas as pd
import os
import plotly
import plotly.graph_objects as go
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler
import pickle as pickle




working_dir = os.path.dirname(os.path.abspath(__file__),)
print(f"Working Directory: {working_dir}")
# ? Folder path
folder_path = f"{working_dir}"
print(f"Folder Path: {folder_path}")
# ? List of files
for f in os.listdir(folder_path):
    if f.endswith(".csv"):
        file_path = os.path.join(folder_path, f)
print(f" printing File path : {file_path}")
data = pd.read_csv(file_path)
print(data.head())
data = data.drop(["Unnamed: 32", "id"], axis=1)
data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})
print(data.head())


def create_model(data):
    X = data.drop(['diagnosis'], axis=1)
    y = data['diagnosis']

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy}")

    mae = mean_absolute_error(y_test, y_pred)
    print(f"MAE: {mae}")

    r2 = r2_score(y_test, y_pred)
    print(f"R2 Score: {r2}")

    classification_report1 = classification_report(y_test, y_pred)
    print(f"Classification Report: {classification_report1}")

    return model, scaler


model, scaler = create_model(data)
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
print("Model and scaler saved as pickle files.")









def add_sidebar():
    st.sidebar.header("Cell Nuclei Measurements")
    slider_labels = [
        ("Radius (mean)", "radius_mean"),
        ("Texture (mean)", "texture_mean"),
        ("Perimeter (mean)", "perimeter_mean"),
        ("Area (mean)", "area_mean"),
        ("Smoothness (mean)", "smoothness_mean"),
        ("Compactness (mean)", "compactness_mean"),
        ("Concavity (mean)", "concavity_mean"),
        ("Concave points (mean)", "concave points_mean"),
        ("Symmetry (mean)", "symmetry_mean"),
        ("Fractal dimension (mean)", "fractal_dimension_mean"),
        ("Radius (se)", "radius_se"),
        ("Texture (se)", "texture_se"),
        ("Perimeter (se)", "perimeter_se"),
        ("Area (se)", "area_se"),
        ("Smoothness (se)", "smoothness_se"),
        ("Compactness (se)", "compactness_se"),
        ("Concavity (se)", "concavity_se"),
        ("Concave points (se)", "concave points_se"),
        ("Symmetry (se)", "symmetry_se"),
        ("Fractal dimension (se)", "fractal_dimension_se"),
        ("Radius (worst)", "radius_worst"),
        ("Texture (worst)", "texture_worst"),
        ("Perimeter (worst)", "perimeter_worst"),
        ("Area (worst)", "area_worst"),
        ("Smoothness (worst)", "smoothness_worst"),
        ("Compactness (worst)", "compactness_worst"),
        ("Concavity (worst)", "concavity_worst"),
        ("Concave points (worst)", "concave points_worst"),
        ("Symmetry (worst)", "symmetry_worst"),
        ("Fractal dimension (worst)", "fractal_dimension_worst"),
    ]

    input_dict = {}

    for label, key in slider_labels:
        input_dict[key] = st.sidebar.slider(
            label,
            min_value=float(0),
            max_value=float(data[key].max()),
            value=float(data[key].mean())
        )

    return input_dict


def get_scaled_values(input_dict):
    X = data.drop(['diagnosis'], axis=1)
    scaled_dict = {}
    for key, value in input_dict.items():
        max_val = X[key].max()
        min_val = X[key].min()
        scaled_value = (value - min_val) / (max_val - min_val)
        scaled_dict[key] = scaled_value

    return scaled_dict

def get_radar_chart(input_data):
    
    input_data = get_scaled_values(input_data)

    categories = ['Radius', 'Texture', 'Perimeter', 'Area',
                'Smoothness', 'Compactness',
                'Concavity', 'Concave Points',
                'Symmetry', 'Fractal Dimension']

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[
            input_data['radius_mean'],input_data['texture_mean'],input_data['perimeter_mean'],input_data['area_mean'],
            input_data['smoothness_mean'],input_data['compactness_mean'],input_data['concavity_mean'],input_data['concave points_mean'],
            input_data['symmetry_mean'],input_data['fractal_dimension_mean']
        ],
        theta=categories,
        fill='toself',
        name='Mean Value'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[
            input_data['radius_se'],input_data['texture_se'],input_data['perimeter_se'],input_data['area_se'],
            input_data['smoothness_se'],input_data['compactness_se'],input_data['concavity_se'],input_data['concave points_se'],
            input_data['symmetry_se'],input_data['fractal_dimension_se']
            ],
        theta=categories,
        fill='toself',
        name='Standard Error'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=[
            input_data['radius_worst'],input_data['texture_worst'],input_data['perimeter_worst'],input_data['area_worst'],
            input_data['smoothness_worst'],input_data['compactness_worst'],input_data['concavity_worst'],input_data['concave points_worst'],
            input_data['symmetry_worst'],input_data['fractal_dimension_worst']
        ],
        theta=categories,
        fill='toself',
        name='Worst Value'
    ))

    fig.update_layout(
        width=500, height=500,
        margin=dict(l=10, r=10, t=10, b=10),
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )),
        showlegend=True
    )
    
    return fig

def add_predictions(input_data):
    model = pickle.load(open('model.pkl', 'rb'))
    scale = pickle.load(open('scaler.pkl', 'rb'))
    
    input_array = np.array(list(input_data.values())).reshape(1,-1)
    input_array_scaled = scale.transform(input_array)
    prediction = model.predict(input_array_scaled)
    
    proba_Benign = model.predict_proba(input_array_scaled)[0][0]*100
    proba_Malicious = model.predict_proba(input_array_scaled)[0][1]*100
    
    st.subheader("Cell cluster prediction")
    st.write("The cell cluster is:")
    
    if prediction[0] == 0:
        st.write(':green[Benign]')
    else:
        st.write(':red[Malicious]')
    if proba_Benign > 50:
        st.write(f"Probability of being :green[Benign]  :  :green[{round(proba_Benign, 2)}%]")
        st.write(f"Probability of being :gray[Malicious]  :  :gray[{round(proba_Malicious, 2)}%]")
    else:
        st.write(f"Probability of being :gray[Benign]  :gray[{round(proba_Benign, 2)}%]")
        st.write(f"Probability of being :red[Malicious]  :red[{round(proba_Malicious, 2)}%]")
    # st.write(f"Probability of being :green[Benign]: :blue[{round(model.predict_proba(input_array_scaled)[0][0]*100, 2)}%]")
    # st.write(f"Probability of being :red[Malicious]: :blue[{round(model.predict_proba(input_array_scaled)[0][1]*100,2)}%]")
    st.divider()
    st.write(":gray[Note:- This app can assist medical professionals in making a diagnosis, but should not be used as a substitute for a professional diagnosis.]")

def main():
    
    st.set_page_config(page_title="Breast Cancer Prediction", page_icon=":female-doctor:", layout="wide")
    #file_path=file_path
    input_data = add_sidebar()
    
    with st.container():
        st.title("Breast Cancer Predictior")
        st.write("""Please connect this app to your cytology lab to help diagnose breast cancer form your tissue sample. 
                This app predicts using a machine learning model whether a breast mass is :blue[Benign] or :blue[Malignant]
                based on the measurements it receives from your cytosis lab. You can also update the measurements by hand using the sliders in the sidebar.""")
        st.divider()

    st.columns((1,1))
    col1, col2 = st.columns((1,1))
    
    with col1:
        radar_chart = get_radar_chart(input_data)
        st.plotly_chart(radar_chart)
    with col2:
        add_predictions(input_data)
    
if __name__ == "__main__":
    main()