import tkinter as tk
from tkinter import *
import pandas as pd
from cx_Oracle import *
con=connect("bus_management/bus")



x=''



def bustablefun(root,frame1,frame2,frame3):

        global x

        if x=='passengertable':
            frame1.destroy
        elif x=='journeytable':
            frame3.destroy

        x='bustable'

        frame2.place(x=200,y=60,width=800,height=380)
        head=Label(frame2,text="Bus details table",font=("sans",13)).place(x=20,y=35)
        t=Text(frame2,width=93,height=18)
        t.place(x=20,y=70)
        d=pd.read_sql_query("select * from bus_detail",con)
        # print(d)
        t.insert(tk.END,d)
        t.config(state="disable")





def journeytablefun(root,frame1,frame2,frame3):

        global x
        if x=='passengertable':
            frame1.destroy

        elif x=='bustable':
            frame2.destroy


        x='journeytable'
        frame2.place(x=200,y=60,width=800,height=380)
        head=Label(frame2,text="Journey details table",font=("sans",13)).place(x=20,y=35)
        t=Text(frame2,width=93,height=18)
        t.place(x=20,y=70)
        d=pd.read_sql_query("select * from journy_detail",con)
        # print(d)
        t.insert(tk.END,d)
        t.config(state="disable")






def passengertablefun(root,frame1,frame2,frame3):

        global x

        if x=='journeytable':
            frame3.destroy
            print("destroyed")
        elif x=='bustable':
            frame2.destroy
            # print("again")


        frame1.place(x=200,y=60,width=800,height=380)
        head=Label(frame1,text="Passenger details table",font=("sans",13)).place(x=20,y=35)
        t=Text(frame1,width=93,height=18)
        t.place(x=20,y=70)
        d=pd.read_sql_query("select * from passenger_detail",con)
        # print(d)

        t.insert(tk.END,d)
        t.config(state="disable")





def adminwindows():
        root=Tk()
        root.geometry("1000x500+160+80")
        frame1=Frame(root)
        frame2=Frame(root)
        frame3=Frame(root)


        h1 = Label(root,text="Admin Windows",font=("sans",18),fg="white",bg="green").place(x=30,y=20,width=940)
        btn1 = Button(root,text="Passenger Table",bg="red",fg="white",font=("sans",14),command=lambda : passengertablefun(root,frame1,frame2,frame3)).place(x=30,y=100,width=150)
        btn2 = Button(root,text="Bus Table",bg="red",fg="white",font=("sans",14),command=lambda : bustablefun(root,frame1,frame2,frame3)).place(x=30,y=170,width=150)
        btn3 = Button(root,text="Journy Table",bg="red",fg="white",font=("sans",14),command=lambda : journeytablefun(root,frame1,frame2,frame3)).place(x=30,y=240,width=150)
        btn4 = Button(root,text="Close",bg="red",fg="white",font=("sans",14),command=root.destroy).place(x=30,y=310,width=150)


        root.mainloop()


# adminwindows()

if  '__name__'=='__main__' :
        adminwindows()
