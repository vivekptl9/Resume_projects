import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
import tkinter
import joblib
import streamlit as st
import os



#? Loading the dataset

insurance_dataset = pd.read_csv('./insurance.csv')

#* first 5 rows of the dataframe
#insurance_dataset.head()
#*Dataframe information
#insurance_dataset.info()
#* Dataframe description
#insurance_dataset.describe()
#* Dataframe shape
#insurance_dataset.shape

#? Checking null values
#insurance_dataset.isnull().sum()

#?  Distribution of of different columns
sns.set()
# plt.figure(figsize=(6, 6))
# sns.displot(insurance_dataset['age'], kde=True)
# plt.title('Age Distribution')
# plt.show()

# plt.figure(figsize=(4, 4))
# sns.countplot(x='sex', data=insurance_dataset, hue='sex')
# plt.title('Gender Distribution')
# plt.show()

# plt.figure(figsize=(6, 6))
# sns.displot(insurance_dataset['bmi'], kde=True)
# plt.title('BMI Distribution')
# plt.show()

# plt.figure(figsize=(4, 4))
# sns.countplot(x='children', data=insurance_dataset, hue='children')
# plt.title('Number of Children Distribution')
# plt.show()

# plt.figure(figsize=(4, 4))
# sns.countplot(x='smoker', data=insurance_dataset, hue='smoker')
# plt.title('Smokers Distribution')
# plt.show()

# plt.figure(figsize=(4, 4))
# sns.scatterplot(x='age',y='smoker', data=insurance_dataset, hue='sex')
# plt.title('Smokers Distribution')
# plt.show()



#? ******************************************************************** STEAMLIT APP ********************************************************************



# ? Set Page Configuration
st.set_page_config(page_title="Data Visualizer",
                   layout="centered",
                   page_icon="📊")

# ? Title

st.title("📊 Data Visualizer - Web App")

# ? Getting the working directory
working_dir = os.path.dirname(os.path.abspath(__file__))
# print(f"Working Directory: {working_dir}")

# ? Folder path
folder_path = f"{working_dir}"
# print(f"Folder Path: {folder_path}")

# ? List of files
files_list = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

# ? Dropdown for all the files
selected_file = st.selectbox("Select a file", files_list, index=None)


if selected_file:
    file_path = os.path.join(folder_path, selected_file)
    #print(file_path)

    df = pd.read_csv(file_path)
    
    df.replace({'sex': {"male":0,"female":1}},inplace =True)
    df.replace({'region': {"southeast": 0, "southwest": 1,
            "northeast": 2, "northwest": 3}}, inplace=True)
    df.replace({'smoker': {"yes": 1, "no": 0}}, inplace=True)
    
#*-------------------------------------------------------------------------------------------------------------------
    X = df.drop(columns="charges", axis=1)
    Y = df['charges']
    
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=2)

#? Fitting the model-------------------------------------------------------------------------------------------------

    # models = {
    #     "Linear Regression": LinearRegression(),
    #     "Random Forest": RandomForestRegressor(),
    #     "Gradient Boosting": GradientBoostingRegressor()
    # }

    model_lin = LinearRegression()
    model_lin.fit(X_train, Y_train)

    model_rf = RandomForestRegressor()
    model_rf.fit(X_train, Y_train)


    model_gr = GradientBoostingRegressor()
    model_gr.fit(X_train, Y_train)
    # r_squared_results = {}
    # for model_name, model in models.items():
    #     model.fit(X_train, Y_train)
    #     y_pred = model.predict(X_test)
    #     r2 = metrics.r2_score(Y_test, y_pred)
    #     r_squared_results[model_name] = r2

#? Model Evaluation on training data-------------------------------------------------------------------------------------------------

    lin_pred_train = model_lin.predict(X_train)
    rf_pred_train = model_rf.predict(X_train)
    gb_pred_train = model_gr.predict(X_train)
    
    r2_lin_train = metrics.r2_score(Y_train, lin_pred_train)
    r2_rf_train = metrics.r2_score(Y_train, rf_pred_train)
    r2_gb_train = metrics.r2_score(Y_train, gb_pred_train)

#? Model Evaluation on testing data-------------------------------------------------------------------------------------------------

    lin_pred_test = model_lin.predict(X_test)
    rf_pred_test = model_rf.predict(X_test)
    gb_pred_test = model_gr.predict(X_test)

    r2_lin_test = metrics.r2_score(Y_test, lin_pred_test)
    r2_rf_test = metrics.r2_score(Y_test, rf_pred_test)
    r2_gb_test = metrics.r2_score(Y_test, gb_pred_test)
    
    mae_lin_test = metrics.mean_absolute_percentage_error(
        Y_test, lin_pred_test)*100
    mae_rf_test = metrics.mean_absolute_percentage_error(Y_test, rf_pred_test)*100
    mae_gb_test = metrics.mean_absolute_percentage_error(Y_test, gb_pred_test)*100
    
    
    r_square_list = [r2_lin_test, r2_rf_test, r2_gb_test]
    mae_list = [mae_lin_test, mae_rf_test, mae_gb_test]
    
    df1 = pd.DataFrame({'Actual': Y_test, 'LR': lin_pred_test, 'RF': rf_pred_test, 'GB': gb_pred_test})
    df_melted2 = df1.melt(var_name='Model', value_name='Value')
    print(df_melted2['Model'].unique())
    st.title("Linear Regression Models For Premium Prediction")
    fig1, ax = plt.subplots(2, 2, sharex='row', sharey='all')
    ax[0, 0].hist(df1['Actual'])
    ax[0, 0].title.set_text("Actual")
    ax[0, 0].tick_params(axis='both', labelsize=7)
    ax[0, 1].hist(df1['LR'])
    ax[0, 1].title.set_text("LR")
    ax[0, 1].tick_params(axis='both', labelsize=7)
    ax[1, 0].hist(df1['RF'])
    ax[1, 0].title.set_text("RF")
    ax[1, 0].tick_params(axis='both', labelsize=7)
    ax[1, 1].hist(df1['GB'])
    ax[1, 1].title.set_text("GB")
    ax[1, 1].tick_params(axis='both', labelsize=7)
    plt.tight_layout()
    st.pyplot(fig1)
    st.header("Model Metrics")
    st.markdown(f"""
                - R-Squared value for Linear Regression Model on Test Data: :blue[{round(r2_lin_test,2)}]
                - R-Squared value for Random Forest Model on Test Data: :blue[{round(r2_rf_test,2)}]
                - R-Squared value for Gradient Boost Model on Test Data: :blue[{round(r2_gb_test,2)}]
                """)
    st.divider()
    st.subheader(f"The best  R-Squared value is: :red[{round(max(r_square_list),2)}]")

    st.markdown(f"""
                - Mean Absolute % Error value for Linear Regression Model on Test Data: :blue[{round(mae_lin_test,2)}%]
                - Mean Absolute % Error value for Random Forest Model on Test Data: :blue[{round(mae_rf_test,2)}%]
                - Mean Absolute % Error value for Gradient Boost Model on Test Data: :blue[{round(mae_gb_test,2)}%]
                """)
    st.divider()
    st.subheader(
        f"The best  Mean Absolute Error value is: :red[{round(min(mae_list),2)}]%")

    st.divider()
    st.title("Model Comparison Plot")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    for model in df_melted2['Model'].unique():
        if model == 'Actual':
            sns.kdeplot(data=df_melted2[df_melted2['Model'] == 'Actual'],
                        x='Value', fill=True, label='Actual', ax=ax2)
        else:
            sns.kdeplot(data=df_melted2[df_melted2['Model'] == model], x='Value', fill=False, label=model,ax =ax2)
        plt.title('Histograms of Different Models')
        plt.legend(title='Model')
    st.pyplot(fig2)
    
    st.title("Want to play with the data?")
    col1, col2 = st.columns(2)
    columns = df.columns.tolist()
    
    with col1:
        st.write("")
        st.write(insurance_dataset.head())
    with col2:
        x_axis = st.selectbox("Select the X-axis",
                            options=columns+["None"], index=None)
        y_axis = st.selectbox("Select the Y-axis",
                            options=columns+["None"], index=None)
        add_on = st.selectbox("Select aditional parameter",
                            options=columns+["None"], index=None)    
        plot_list = ["Line Plot", "Bar Chart",
                    "Scatter Plot", "Distribution Plot", "Count Plot"]

        selected_plot = st.selectbox(
            "Selected a Plot", options=plot_list, index=None)
        
    if st.button("Generate Plots"):
        fig, ax = plt.subplots(figsize=(6, 4))

        if selected_plot == "Line Plot":
            sns.lineplot(x=df[x_axis], y= df[y_axis], hue=df[add_on], ax=ax)

        elif selected_plot == "Bar Chart":
            sns.barplot(x=df[x_axis], y=df[y_axis],hue=df[add_on], ax=ax)

        elif selected_plot == "Scatter Plot":
            sns.scatterplot(x= df[x_axis], y=df[y_axis], hue=df[add_on], ax=ax)

        elif selected_plot == "Distribution Plot":
            sns.histplot(x= df[x_axis],hue=df[add_on], kde=True, ax=ax)

        elif selected_plot == "Count Plot":
            sns.countplot(x=df[x_axis], hue=df[add_on], ax=ax)

        ax.tick_params(axis="x", labelsize=10)
        ax.tick_params(axis="y", labelsize=10)

        plt.title(f"{selected_plot} of {y_axis} vs {x_axis}", fontsize=12)
        plt.xlabel(x_axis, fontsize=10)
        plt.ylabel(y_axis, fontsize=10)
        st.pyplot(fig)
        
    