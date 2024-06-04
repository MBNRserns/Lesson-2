#importing tkinter module
from tkinter import * 
from tkinter.ttk import *

#creating tkinter window
root = Tk()

W = Spinbox(root, from_=0, to=100)
W.pack()

mainloop()