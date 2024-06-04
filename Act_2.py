#importing tkinter module
from tkinter import * 
from tkinter.ttk import *
import time

#creating tkinter window
root = Tk()

#progress bar
progress=Progressbar(root,orient=HORIZONTAL,length=100,mode='determinate')

#function bar
def bar():
    progress['value']=20
    root.update_idletasks()
    time.sleep(1)
    progress['value']=40
    root.update_idletasks()
    time.sleep(1)
    progress['value']=60
    root.update_idletasks()
    time.sleep(1)
    progress['value']=80
    root.update_idletasks()
    time.sleep(1)
    progress['value']=100
    root.update_idletasks()
    time.sleep(1)


#create button
Button(root,text="Start",command=bar).pack(pady=10)


progress.pack(pady=10)
mainloop()