import tkinter as tk
from tkinter import ttk

# Create the root window
root = tk.Tk()

# Correct full path to the .tcl file
theme_path = r"d:\Resume_projects\Python_Practice\Python_GUI\forest-dark.tcl"
combo_list = ["Subscribed", "Not Subscribed", "Other"]

# Load the .tcl file as a script
try:
    root.tk.call("source", theme_path)  # Source the .tcl file
    ttk.Style(root).theme_use("forest-dark")  # Apply the theme
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

# Run the application
root.mainloop()
