import tkinter as tk
from tkinter import ttk
import openpyxl

# Create the root window
root = tk.Tk()
style =ttk.Style(root)
# Correct full path to the .tcl file
theme_path_d = r"d:\Resume_projects\Python_Practice\Python_GUI\forest-dark.tcl"
theme_path_l = r"d:\Resume_projects\Python_Practice\Python_GUI\forest-light.tcl"
combo_list = ["Subscribed", "Not Subscribed", "Other"]

def toggle_mode():
    if mode_switch.instate(["selected"]):
        style.theme_use("forest-light")
    else:
        style.theme_use("forest-dark")
        
        
def load_data():
    path = r"d:\Resume_projects\Python_Practice\Python_GUI\people.xlsx"
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active

    list_values = list(sheet.values)
    print(list_values)
    for col_name in list_values[0]:
        treeview.heading(col_name, text=col_name)

    for value_tuple in list_values[1:]:
        treeview.insert('', tk.END, values=value_tuple)
    
# Load the .tcl file as a script
try:
    root.tk.call("source", theme_path_d)  # Source the .tcl file
    style.theme_use("forest-dark")  # Apply the theme
except tk.TclError as e:
    print(f"Error: {e}")
    
try:
    root.tk.call("source", theme_path_l)  # Source the .tcl file
   # style.theme_use("forest-light")  # Apply the theme
except tk.TclError as e:
    print(f"Error: {e}")

# # Example UI to test the theme
# label = ttk.Label(root, text="Hello, Forest Dark Theme!")
# label.pack(padx=20, pady=20)

# button = ttk.Button(root, text="Click Me")
# button.pack(padx=20, pady=20)
frame = ttk.Frame(root)
frame.pack()

widgets_frame = ttk.LabelFrame(frame,text="Insert Row")
widgets_frame.grid(row=0,column=0,padx=20,pady=10)

name_entry = ttk.Entry(widgets_frame)
name_entry.insert(0,"Name")
name_entry.bind("<FocusIn>", lambda e: name_entry.delete("0","end"))
name_entry.grid(row=0,column=0,padx=5, pady=(0,5),sticky="ew")


age_spinbox = ttk.Spinbox(widgets_frame, from_=18, to= 100)
age_spinbox.grid(row=1, column=0, padx=5, pady=5,sticky="ew")
age_spinbox.insert(0, "Age")

status_combobox = ttk.Combobox(widgets_frame, values=combo_list)
status_combobox.current(0)
status_combobox.grid(row=2, column=0,  padx=5, pady=5, sticky="ew")

a=tk.BooleanVar()
checkbutton = ttk.Checkbutton(widgets_frame,text="Employed", variable=a)
checkbutton.grid(row=3, column=0,  padx=5, pady=5, sticky="nsew")

button = ttk.Button(widgets_frame,text="Insert")
button.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

seperator = ttk.Separator(widgets_frame)
seperator.grid(row=5,column=0, padx=(20,10),pady=10,sticky="ew")

mode_switch = ttk.Checkbutton(
    widgets_frame, text="Mode", style="Switch", command=toggle_mode)
mode_switch.grid(row=6,column=0,padx=5,pady=10,sticky="nsew")


treeFrame = ttk.Frame(frame)
treeFrame.grid(row=0, column=1, pady=10)
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

cols = ("Name", "Age", "Subscription", "Employment")
treeview = ttk.Treeview(treeFrame, show="headings",
                        yscrollcommand=treeScroll.set, columns=cols, height=13)
treeview.column("Name", width=100)
treeview.column("Age", width=50)
treeview.column("Subscription", width=100)
treeview.column("Employment", width=100)
treeview.pack()
treeScroll.config(command=treeview.yview)
load_data()


# Run the application
root.mainloop()
