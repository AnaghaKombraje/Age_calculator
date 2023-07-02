#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
from PIL import Image,ImageTk
from datetime import date
import calendar
import datetime
import tkinter as tk
window=Tk()
window.geometry("520x480")
var=IntVar()
def display():
    op=var.get()
    if op==1:#age calculator
        root=Tk()    #creating window
        root.title("AGE-CALCULATOR")   #setting up title
        root.configure(bg="light blue")   #setting up backround color
        root.geometry("400x300")    #fixing the size of the window
        new=Label(root,bg="light blue")  #declaring a lable
        new.grid(row=5,column=0,columnspan=3)
        today=str(date.today())    #getting current date using datetime module
        list_today=today.split("-")  #converting into a list
        def age(b_date,b_month,b_year):#defining a function to calcutate age
            global today
            b_date=int(entry_date.get())
            b_month=int(entry_month.get())
            b_year=int(entry_year.get())
            c_date=int(list_today[2])
            c_month=int(list_today[1])
            c_year=int(list_today[0])
            month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if(b_date>c_date):
                c_month=c_month-1
                c_date=c_date+month[b_month-1]
            if (b_month>c_month):
                c_year=c_year-1
                c_month=c_month+12
            resultd=str(c_date-b_date)
            resultm=str(c_month-b_month)
            resulty=str(c_year-b_year)
            new=Label(root,text="YOUR AGE \n"+resulty+" YEARS "+resultm+" MONTHS "+ resultd+" DAYS ",fg="dark magenta",bg="#D5C6FF",borderwidth=6)
            new.config(font=("Arial Rounded MT Bold",15))
            new.grid(row=5,column=0,columnspan=3)
        title_label=Label(root,text="AGE CALCULATOR",borderwidth=10,fg="dark violet",bg="light blue",font=("Broadway",29))
        title_label.grid(row=0,column=0,columnspan=3)
        label_date=Label(root,text="BIRTH DATE : ",borderwidth=4,fg="dark magenta",bg="light blue",font=("Arial Rounded MT Bold",15))
        label_date.grid(row=1,column=0)
        label_month=Label(root,text="BIRTH MONTH : ",borderwidth=5,fg="dark magenta",bg="light blue",font=("Arial Rounded MT Bold",15))
        label_month.grid(row=2,column=0)
        label_year=Label(root,text="BIRTH YEAR : ",borderwidth=9,fg="dark magenta",bg="light blue",font=("Arial Rounded MT Bold",15))
        label_year.grid(row=3,column=0)
        entry_date=Entry(root,width=20,borderwidth=3)
        entry_month=Entry(root,width=20,borderwidth=3)
        entry_year=Entry(root,width=20,borderwidth=3)
        entry_date.grid(row=1,column=2)
        entry_month.grid(row=2,column=2)
        entry_year.grid(row=3,column=2)
        b_date=entry_date.get()
        b_month=entry_month.get()
        b_year=entry_year.get()
        submit=Button(root,text="GET AGE!!",width=10,anchor=CENTER,command=lambda:age(b_date,b_month,b_year),bg="dark violet",fg="white",borderwidth=5)
        submit.grid(row=4,column=0)
    if op==2:
        def showCal() :
            new_gui = Tk()
            new_gui.config(background = "light blue")
            new_gui.title("CALENDAR")
            new_gui.geometry("550x600")#configuration
            fetch_year = int(year_field.get())
            cal_content = calendar.calendar(fetch_year)# the calendar of the given year 
            cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold")
            cal_year.pack(side=LEFT)
#             aa1=Label(new_gui,text="\n\n\n\n\n\n\n\n",bg="light blue").pack(side=TOP)
#             a1=Label(new_gui,text="14-01:Makara Sankranthi",bg="light blue",font=13).pack(side=TOP)
#             a2=Label(new_gui,text=" 28-02:National Science Day",bg="light blue",font=13).pack(side=TOP)
#             a3=Label(new_gui,text="03-03:World Wildlife Day",bg="light blue",font=13).pack(side=TOP)
#             a4=Label(new_gui,text="07-04:World Health Day",bg="light blue",font=13).pack(side=TOP)
#             a5=Label(new_gui,text="     01-05:International Labour Day",bg="light blue",font=13).pack(side=TOP)
#             a6=Label(new_gui,text="    05-06:World Environment Day",bg="light blue",font=13).pack(side=TOP)
#             a7=Label(new_gui,text="     04-07:National Doctor’s day",bg="light blue",font=13).pack(side=TOP)
#             a8=Label(new_gui,text="      12-08:International Youth day",bg="light blue",font=13).pack(side=TOP)
#             a9=Label(new_gui,text="16-09:World Ozone Day",bg="light blue",font=13).pack(side=TOP)
#             a10=Label(new_gui,text="03-10:World nature day",bg="light blue",font=13).pack(side=TOP)
#             a11=Label(new_gui,text="19-11:World Citizen day",bg="light blue",font=13).pack(side=TOP)
#             a12=Label(new_gui,text="10-12:Human Right Day",bg="light blue",font=13).pack(side=TOP)
        gui = Tk()
        gui.config(background = "white")# Set the background colour
        gui.title("CALENDAR")
        gui.geometry("250x140")# configuration
        cal = Label(gui, text = "CALENDAR", bg = "light pink",font = ("times", 28, 'bold')).pack()# Create a CALENDAR
        year = Label(gui, text = "Enter Year", bg = "light blue").pack()
        year_field = Entry(gui)# Enter Year
        Show = Button(gui, text = "Show Calendar", fg = "Black",bg = "light blue", command = showCal)
        year_field.pack()
        Show.pack()
l1=Label(window,text="Welcome to the multipurpose GUI Window",font=30,bg="light cyan").pack()
r1=Radiobutton(window,text="Age calculator",font=19,fg="red",variable=var,value=1,command=display).pack()
r2=Radiobutton(window,text="Calendar",font=19,fg="red",variable=var,value=2,command=display).pack()
window.configure(bg="misty rose")
window.mainloop()


# In[ ]:




