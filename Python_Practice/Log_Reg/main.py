import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler
import pickle as pickle





#? Data Cleaning----------------------------------------


def get_clean_data():
    working_dir = os.path.dirname(os.path.abspath(__file__))

# print(f"Working Directory: {working_dir}")
# ? Folder path
    folder_path = f"{working_dir}"
# print(f"Folder Path: {folder_path}")
# ? List of files
    for f in os.listdir(folder_path):
        if f.endswith(".csv"):
            file_path = os.path.join(folder_path, f)
# print(f" printing File path : {file_path}")
        data = pd.read_csv(file_path)
    #print(data.head())
        data = data.drop(["Unnamed: 32", "id"], axis=1)
    
        data['diagnosis'] = data['diagnosis'].map({'M':1,'B':0})
    
    return data


def create_model(data):
    X = data.drop(['diagnosis'], axis=1)
    y = data['diagnosis']
    
    scaler = StandardScaler()
    X =scaler.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
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
    
    return model,scaler


    



def main():
    data = get_clean_data()
    model,scaler = create_model(data)
    
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)

    print("Model and scaler saved as pickle files.")
    
    
    
if __name__ == "__main__":
    main()