current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
file_path= ""
for f in os.listdir(parent_dir):
    if f.endswith(".csv"):
        file_path = os.path.join(parent_dir, f)
data = pd.read_csv(file_path)