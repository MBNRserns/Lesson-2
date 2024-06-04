from tkinter import *
# Tk themed widget set
from tkinter.ttk import *
from time import strftime

# creating tkinter window
root= Tk()
root.title('Menu Demonstration')

#creating menubar
menubar=Menu(root)

# Adding file menu and commands
#a tearoff permits you to detach menus for the most window making floating menus
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)
file.add_command(label='New FIle', command=None) #nothing happens when clicked
file.add_command(label='Open', command=None)
file.add_command(label='Save', command=None)
file.add_separator()
file.add_command(label='Exit', command=root.destroy) #window closes

edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=edit)
edit.add_command(label='Cut', command=None) #nothing happens when clicked
edit.add_command(label='Copy', command=None)
edit.add_command(label='Paste', command=None)
edit.add_command(label='Select All', command=None)
edit.add_separator()
edit.add_command(label='Find', command=None)
edit.add_command(label='Find again', command=None)

help=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=help)
help.add_command(label='Tk Help', command=None) #nothing happens when clicked
help.add_command(label='Demo', command=None)
help.add_separator()
help.add_command(label='About Tk', command=None)


#display Menu
root.config(menu=menubar)
mainloop()