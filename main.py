from tkinter import *
from tkinter import filedialog
from tkinter import font
import sys
import os

# Function to locate resources in both .py and .exe
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller uses this
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root = Tk()
root.title("Harshal's Notepad")
icon_path = resource_path("Notepad_22522.ico")
root.iconbitmap(icon_path)
root.geometry("500x500")

# Menu Bar
menu = Menu(root)
root.config(menu=menu)

# Save file
current_file_path = None

def new_file():
    text_area.delete("1.0", "end")
    global current_file_path
    current_file_path = None

def open_file_dialog():
    global current_file_path
    current_file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if current_file_path:
        process_file(current_file_path)

def process_file(file_path):
    try:
        with open(file_path, "r") as file:
            file_contents = file.read()
            text_area.delete("1.0", "end")
            text_area.insert(END, file_contents)
    except Exception as e:
        print(f"Error opening file : {e}")

def save_as():
    file_path = filedialog.asksaveasfilename(filetypes=[("Text File", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            file_content = text_area.get("1.0", END)
            with open(file_path, "w") as file:
                file.write(file_content)
        except Exception as e:
            print(f"Error saving file : {e}")

def save_file():
    if current_file_path:
        try: 
            file_content = text_area.get("1.0", END)
            with open(current_file_path, "w") as file:
                file.write(file_content)
        except Exception as e:
            print(f"Error saving file : {e}")
    else:
        save_as()

# Edit menu functions
def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

def delete_text():
    text_area.delete("sel.first", "sel.last")

def selectall_text():
    text_area.tag_add("sel", "1.0", "end")

# Find function
def find_text():
    find_window = Toplevel(root)
    find_window.title("Find")
    find_window.geometry("280x90")
    find_window.transient(root)
    find_window.resizable(False, False)
    current_search_index = "1.0"

    def close_window():
        text_area.tag_remove("match", "1.0", END)  # remove highlight on close
        find_window.destroy()  # destroy the actual Toplevel window

    def search():
        text_area.tag_remove("match", "1.0", END)
        keyword = find_entry.get()
        if keyword:
            idx = "1.0"
            while True:
                idx = text_area.search(keyword, idx, nocase=1, stopindex=END)
                if not idx:
                    break
                end_idx = f"{idx}+{len(keyword)}c"
                text_area.tag_add("match", idx, end_idx)
                idx = end_idx
            text_area.tag_config("match", foreground="red", background="yellow")

    def replace_text():
        text_area.tag_remove("match", "1.0", END)
        keyword = find_entry.get()
        replace_keyword = replace_entry.get()
        nonlocal current_search_index
        if keyword:
            idx = text_area.search(keyword, current_search_index, nocase=1, stopindex=END)
            if idx:
                end_idx = f"{idx}+{len(keyword)}c"
                text_area.delete(idx, end_idx)
                text_area.insert(idx, replace_keyword)
                text_area.tag_add("match", idx, end_idx)
                current_search_index = end_idx
            else:
                current_search_index = "1.0"

    Label(find_window, text="Find:", font="Arial 10 bold").place(x=10, y=20, anchor=W)
    find_entry = Entry(find_window)
    find_entry.place(x=80, y=10)

    Label(find_window, text="Replace:", font="Arial 10 bold").place(x=10, y=60, anchor=W)
    replace_entry = Entry(find_window)
    replace_entry.place(x=80, y=50)

    Button(find_window, text=">", command=search).place(x=240, y=10)
    Button(find_window, text="<", command=replace_text).place(x=220, y=10)

    find_window.protocol("WM_DELETE_WINDOW", close_window)

font_size = 9

def zoom_in():
    global font_size
    font_size += 2
    text_font.configure(size=font_size)

def zoom_out():
    global font_size
    font_size -= 2
    text_font.configure(size=font_size)

# File menu
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label='New', command=new_file)
filemenu.add_command(label='Open', command=open_file_dialog)
filemenu.add_command(label='Save', command=save_file)
filemenu.add_command(label='Save as', command=save_as)
filemenu.add_command(label='Print')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

# Edit menu
editmenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=cut_text)
editmenu.add_command(label='Copy', command=copy_text)
editmenu.add_command(label='Paste', command=paste_text)
editmenu.add_command(label='Delete', command=delete_text)
editmenu.add_command(label='Find', command=find_text)
editmenu.add_command(label='Select all', command=selectall_text)

# View menu
viewmenu = Menu(menu)
menu.add_cascade(label='View', menu=viewmenu)
viewmenu.add_command(label='Zoom in', command=zoom_in)
viewmenu.add_command(label='Zoom out', command=zoom_out)

# Scrollbar and Text area
scroll_bar = Scrollbar(root)
scroll_bar.pack(side=RIGHT, fill=Y)



text_font = font.Font(root, family="Arial", size=font_size)
text_area = Text(root, yscrollcommand=scroll_bar.set, font=text_font)


text_area.pack(fill=BOTH, expand=True)
scroll_bar.config(command=text_area.yview)

root.mainloop()
