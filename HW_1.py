from tkinter import *
from tkinter.ttk import *
import time

root = Tk()
root.geometry('500x500')
root.title("Food Delivery App")
root.config(background="red")

#label for username
email=Label(root,text = "Email").place(x=40, y=20)
email_entry_area= Entry(root,width=30).place(x=110,y=20)

#label for password
password=Label(root,text = "Password").place(x=40, y=50)
password_entry_area= Entry(root,width=30,show="*").place(x=110, y=50)

#label for Food
food=Label(root,text = "What food would you like? 1.Chicken Sandwich, 2. B.L.T, 3. Veggie Sandwich, or 4. None").place(x=20, y=90)
food_entry_area= Entry(root,width=30).place(x=25, y=120)
W = Spinbox(root, from_=0, to=4).place(x=230, y=120)


#label for Drink
drink=Label(root,text = "Which drink would you like? 1.Cola, 2. Fanta, 3. Orange juice, or 4. None").place(x=35, y=160)
drink_entry_area= Entry(root,width=30).place(x=25, y=190)
W = Spinbox(root, from_=0, to=4).place(x=230, y=190)

#label for Dessert
drink=Label(root,text = "Which dessert would you like? 1.Ice Cream, 2. Ice Lolly, 3. Chocolate Cake, or 4. None").place(x=35, y=220)
drink_entry_area= Entry(root,width=30).place(x=25, y=250)
W = Spinbox(root, from_=0, to=4).place(x=230, y=250)


#progress bar
progress=Progressbar(root,orient=HORIZONTAL,length=100,mode='determinate').place(x=170,y=390)

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
Button(root,text="Submit Order",command=bar).place(x=170,y=340)






root.mainloop()