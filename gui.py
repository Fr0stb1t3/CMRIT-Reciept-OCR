import tkinter as tk
from tkinter.filedialog import askopenfilename
root = tk.Tk()
canvas = tk.Canvas(root, width = 1280, height =720)
canvas.grid(columnspan=10, rowspan=10)

#text
instructions = tk.Label(root, text = "Select a File from your Computer to Convert")
instructions.grid(columnspan=10, column = 0, row = 0)

#function to get pathname of selected file
def openFile():
    browse_text.set("Loading..")
    file_path = askopenfilename()
    
    #if file is selected
    if file_path:
        browse_text.set("File Selected")
        browse_button.configure(state="disable")

        #display the pathname of the selected file
        filePath_display = tk.Label(root, text=file_path)
        filePath_display.grid(columnspan=10, column=0, row =2)

        #convert button
        convert_text = tk.StringVar()
        convert_button = tk.Button(root, textvariable=convert_text, height=2, width=15)
        convert_text.set("Convert")
        convert_button.grid(columnspan=10, column=0, row=3)
    
#browse button
browse_text = tk.StringVar()
browse_button = tk.Button(root, textvariable=browse_text, command = lambda: openFile(), height = 2, width = 15)
browse_text.set("Browse")
browse_button.grid(columnspan = 10, column=0, row = 1)
root.mainloop()
