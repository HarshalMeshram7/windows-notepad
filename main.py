from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Harshal's Notepad")
root.iconbitmap("Notepad_22522.ico")
root.geometry("500x500")

#Menu Bar
menu = Menu(root)
root.config(menu=menu)

#Newfile menu function
def new_file():
    text_area.delete("1.0", "end")

#open_file
def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        process_file(file_path)
   
def process_file(file_path):
    try:
        with open(file_path, "r") as file:
            file_contents = file.read()
            text_area.delete("1.0", "end")
            text_area.insert(END, file_contents)
    except Exception as e:
        print(f"Error opening file : {e}")
        

#filemenu buttons
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label='New', command=new_file)
filemenu.add_command(label='Open', command=open_file_dialog)
filemenu.add_command(label='Save')
filemenu.add_command(label='Save as')
filemenu.add_command(label='Print')
filemenu.add_command(label='Close')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

#editmenu buttons
editmenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')
editmenu.add_command(label='Delete')
editmenu.add_command(label='Find')
editmenu.add_command(label='Select all')

#viewmenu buttons
viewmenu = Menu(menu)
menu.add_cascade(label='View', menu=viewmenu)
viewmenu.add_command(label='Zoom in')
viewmenu.add_command(label='Zoom out')

# Scrollbar
scroll_bar = Scrollbar(root)
scroll_bar.pack(side=RIGHT, fill=Y)

# Text window
text_area = Text(root, yscrollcommand=scroll_bar.set)
text_area.pack(fill=BOTH, expand=True)

# Scrollbar config
scroll_bar.config(command=text_area.yview)


root.mainloop()