#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:08:05 2019

@author: susmit
"""

from tkinter import *
from tkinter.font import Font

app = Tk()
app.title("All in One")
app.geometry("500x500")

def show_mssg():
    mssg = Message(app)
    mssg.config(text="Hi there!",font=Font(family="ariel",size=21))
    mssg.pack()

def show_mssg_box():
    messagebox.showinfo("Message","Hey!")
    
def show_txt_typed():
    lbl1.config(text=e_txt.get())
    
botFrame = Frame(app,width=300,height=300,bg="blue")
botFrame.pack(side=BOTTOM)
    
btn1 = Button(botFrame,text="Message",bg="yellow",fg="purple",command=show_mssg)
btn1.grid(row=0,column=0)

btn2 = Button(botFrame,text="Message Box",bg="blue",fg="red",command=show_mssg_box)
btn2.grid(row=0,column=1)

lbl1 = Label(app)
lbl1.config(text="Name: ",fg="blue")
lbl1.pack()

e_txt = StringVar()
e = Entry(app,textvariable=e_txt,)
e.pack()

btn3 = Button(botFrame,text="Click after typing",bg="blue",fg="red",command=show_txt_typed)
btn3.grid(row=0,column=2)

gen_male = BooleanVar(value=True)

rb1 = Radiobutton(app,text="Male",var=gen_male,value=True)
rb2 = Radiobutton(app,text="Female",var=gen_male,value=False)
rb1.pack()
rb2.pack()

lbl2 = Label(app)
lbl2.config(text="Hobbies: ",fg="green")
lbl2.pack()

hobby_chess = BooleanVar()
hobby_ds = BooleanVar()

chk_chess = Checkbutton(app,text="Chess",var=hobby_chess)
chk_ds = Checkbutton(app,text="DS",var=hobby_ds)

chk_chess.pack()
chk_ds.pack()

scale_var = IntVar()
scale = Scale(app,var=scale_var,orient="horizontal",from_=0,to=10,resolution=1)
scale.pack()


mb = Menubutton(app,text="Expertise",relief=RAISED)
menu = Menu(mb)
mb.menu = menu
mb["menu"]=menu

dev_des = BooleanVar(value=True)

mb.menu.add_radiobutton(label="Developer",var=dev_des,value=True)
mb.menu.add_radiobutton(label="Designer",var=dev_des,value=False)

mb.pack()


txt = Text(app)
txt.insert(INSERT, "FROM GUI: ")
txt.config(height=10)
txt.pack()





app.mainloop()
