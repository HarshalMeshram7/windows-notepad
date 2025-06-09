from tkinter import *

root = Tk()
root.title("Harshal's Notepad")
root.iconbitmap("Notepad_22522.ico")
root.geometry("500x500")

#Menu Bar

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_command(label='Save as')
filemenu.add_command(label='Print')
filemenu.add_command(label='Close')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

editmenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')
editmenu.add_command(label='Delete')
editmenu.add_command(label='Find')
editmenu.add_command(label='Select all')

viewmenu = Menu(menu)
menu.add_cascade(label='View', menu=viewmenu)
viewmenu.add_command(label='Zoom in')
viewmenu.add_command(label='Zoom out')

# Text window
text_area = Text(root)
text_area.pack(fill=BOTH, expand=True)

# Scrollbar
scroll_bar = Scrollbar(root)
scroll_bar.pack(side=RIGHT, fill=Y)

root.mainloop()