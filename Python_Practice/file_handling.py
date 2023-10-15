import os
path = "D:\\Resume_projects\\test.txt"
path2 ="D:\\Resume_projects\\Python_Practice" 

if os.path.exists(path):
    print("the path exists")
    if os.path.isfile(path):
        print("File exists")
        print(path)
if os.path.isdir(path2):
    print("Directory exists")
    print(path2)
else:
    print("the path Do not exist")
    
#?-----------------------------------------------------------------------------------
try:
    with open("D:\\Resume_projects\\test.tx") as file:
        print(file.read())
except FileNotFoundError:
    print("this file does not exist")