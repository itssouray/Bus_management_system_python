from tkinter import *
from PIL import Image,ImageTk         #pillow
from tkinter import messagebox
from loading import loadingfun          #user module
import cx_Oracle as co
from databasetable import adminwindows
import uuid                         #UNIQUE NUMBER GENERATOR---------------------




# 58ab5
# class
# df63c
# 5d199
# 43e45

# root1=''
root =''
root4 =''
root3 =''

user1 = "bus"
password1 = "1234"

administrator = "admin"
Apassword = "6979"

def verifyUser(root1,user2,password2):
          a = user2.get()
          b = password2.get()



          if (administrator==a):
                if (Apassword==b):
                    root1.destroy()
                    adminwindows()
                else:
                    print("invalid password")

          elif (user1==a and password1==b):
                    print("login successful")
                    root1.destroy()
                    homeScreen()

          elif (a =="" or b==""):
                    print("invalid username or password")
          else :
                    print("Username is Incorrect")





def loginpage(root4):
    root4.destroy()
    callloginfun()

def homepage(rootWindow):
    rootWindow.destroy()
    homeScreen()


def passengerInfo():
    root4.destroy()
    checkDetail()

def busBooking():
    root4.destroy()
    buslist_fun()


def searchfun(id):
        Id = id.get()
        print(Id)
        sqlcmd = "select * from passenger_detail where passenger_id=:id"
        cur.execute(sqlcmd,id=Id)
        x=cur.fetchone()
        print(x)




#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------




def callloginfun():

     root1=Tk()
     root1.geometry("900x500+180+100")
     root1.resizable(0,0)
     root1.config(bg="lavender")

     # root1.
     user2 = StringVar()
     password2 = StringVar()

     x = ImageTk.PhotoImage(file="loginimage2.jpg")


     frame1 = Label(root1,image=x,bg="black").place(width=950,height=550,x=0,y=0)

     loginbox = Frame(frame1,bg="white smoke").place(x=530,y=50,width=320,height=380)

     head = Label(frame1,text="Login Here",font=("sans",20),bg="white smoke").place(x=635,y=90)
     loginLine = Frame(frame1,bg="cyan4").place(x=685,y=128,width=27,height=4)


     username = Label(loginbox,text="Username",bg="white smoke",font=("sans",13)).place(x=560,y=190)
     usernameEntry = Entry(frame1,bg="white",font=("sans",12),textvariable=user2).place(x=650,y=190,width=170)

     password = Label(loginbox,text="Password",bg="white smoke",font=("sans",13)).place(x=560,y=240)
     passwordEntry = Entry(loginbox,bg="white",show="*",font=("sans",12),textvariable=password2).place(x=650,y=240,width=170)


     submit = Button(loginbox,text="Submit",bg="#04604d",font=("Sitka Small Semibold",13),fg="white",width=13,command=lambda : verifyUser(root1,user2,password2)).place(x=630,y=330)

     root1.mainloop()



#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------



def homeScreen():

         global root4
         root4 = Tk()
         root4.resizable(0,0)
         root4.geometry("700x450+300+150")
         heading = Label(root4,text="Bus Management System",font=("Times New Roman",14),fg="white",bg="green").place(x=80,y=10,width=400,height=40)
         z = ImageTk.PhotoImage(file="backbuttonarrow.png")
         backbutton = Button(root4,image=z,bg="white smoke",bd=0,command=lambda : loginpage(root4)).place(x=32,y=10,width=45,height=45)

         frame1 = Frame(root4,bg="white").place(x=30,y=65,width=450,height=360)
         x = ImageTk.PhotoImage(file="C:/Users/itsso/Downloads/pexels-caio-45923 (1).jpg")
         y = Label(frame1,image=x).place(x=30,y=65)

         passengerDetail = Button(root4,text="Passenger Detail",font=("Source Serif Pro Semibold",13),bg="white",command=passengerInfo).place(x=505,y=100,width=170)
         book_Bus = Button(root4,text="Book Bus",font=("Source Serif Pro Semibold",13),bg="white",command=busBooking).place(x=505,y=170,width=170)
         exit = Button(root4,text="Exit",font=("Source Serif Pro Semibold",13),bg="brown3",fg="white",command=root4.destroy).place(x=505,y=240,width=170)

         root4.mainloop()


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

#getting passenger details through booking _____________________________________

con = co.connect("bus_management/bus")
cur = con.cursor()

price = int()
ticket_No = int()
seat_No = int()




#generating ticket No---------------------------------------
def ticketGen():
       numA=uuid.uuid4()
       numB=str(numA)
       numC=numB[1:3]
       num = ''

       for i in numC:
           num += str(ord(i));

       if len(num)>6:
          x=num[:-1]
          ticket_No = int(x)
       else :
          ticket_No = int(num)

       return ticket_No



#generatin passenger Id-----------------------------------
def idGen():
        numA=uuid.uuid4()
        numB=str(numA)
        numC=numB[0:5]
        num = ''

        for i in numC:
            num+=i

        return num;



#inserting ticket price------------------------------------
def checkPrice(busNo):

        if busNo == 101:
            price = 1500

        elif busNo == 202:
            price = 1900

        elif busNo == 303:
            price = 2000

        elif busNo == 404:
            price = 3800

        elif busNo == 505:
            price = 2200

        elif busNo == 606 :
            price = 3200

        return price;



#generating seat No----------------------------------------

def calcSeatNo(busNo):

            select = '''select total_seat,avalable_seat from bus_detail where bus_no= :no'''
            cur.execute(select,no=busNo)
            x=cur.fetchall()
            print(x)
            a=x[0][0]       #total seat
            b=x[0][1]       #available seat

            if b<=0 :
                print("seat not available!")
            else :
                seat_No=b       #inserting the current available seat value into seat_no
                # b-=1            #decrementing available seat
                return seat_No


#-------------------------------------------------------------------------------

#inserting data from fillup form into database ________________________________-

def inserting_into_database(ticketNo,seatNo,seatType,Price,busNo,passenger):

            print("inserting into data base")
            selectbus = '''select total_seat,avalable_seat from bus_detail where bus_no= :no'''
            cur.execute(selectbus,no=busNo)
            x=cur.fetchall()

            b=x[0][1]
            b-=1
            passengerId = idGen()
            Pname=passenger[0]
            Psex=passenger[1]
            Pcontact=passenger[2]
            Page=passenger[3]

            update = '''update bus_detail set avalable_seat = :new where bus_no = :No'''
            cur.execute(update,{"new":b , "No":busNo})

            selectticket = '''insert into ticket_detail values(:ticket_no,:seat_no,:seat_type,:price)'''
            cur.execute(selectticket,[ticketNo,seatNo,seatType,Price])

            selectPassenger = '''insert into passenger_detail values(:id,:name,:age,:sex,:contact,:busno,:ticketno)'''
            cur.execute(selectPassenger,[passengerId,Pname,Page,Psex,Pcontact,busNo,ticketNo])

            con.commit()


#-------------------------------------------------------------------------------

#after clicking close button on receipt windows the passenger details from the form is get
#reflacted into database using inserting_into_database function i.e a commit occure--------------------------------------

def closefunction(receiptRoot,root,ticketNo,seatNo,seatType,Price,busNo,passenger):


                inserting_into_database(ticketNo,seatNo,seatType,Price,busNo,passenger)
                print("destroying all roots")
                root.destroy()
                receiptRoot.destroy()








def onSubmit(name,age,z,contact):
    Pname = name.get()
    P_age = int(age.get())
    Pcontact = contact.get()
    s = int(z.get())
    if s==1:
        sex = 'M'
    elif s==2:
        sex = 'F'

    if(Pname=='' or P_age=='' or Pcontact==''):
        print("please enter the details first")
        return 0;
    else :
        return Pname,sex,int(Pcontact),P_age







#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------


#after submiting from a receipt will poped up ----------------------------------

def receiptcall(submitButton,name,age,z,contact,root,bus,journy):

    personDetails = onSubmit(name,age,z,contact)


    if personDetails==0 :
           return;
    else :

           ticketNo = ticketGen()
           seatNo = calcSeatNo(bus[0])
           Price = checkPrice(bus[0])

           print(personDetails)
           submitButton['state']='disable'
           submitButton.config(bg='lightgray')

           receiptRoot = Tk()
           receiptRoot.geometry("335x565+750+30")
           receiptRoot.resizable(0,0)

           rightframe = Frame(receiptRoot,bg="white").place(x=10,y=10,width=315,height=380)
           rightlabel = Label(receiptRoot,text="Ticket Receipt",fg="green",bg="white",font=("Source Serif Pro Semibold",16)).place(x=100,y=15)


           busno = Label(receiptRoot,text=bus[0],bg="white",fg="red",font=("Source Serif Pro Light",11)).place(x=30,y=60)
           busname = Label(receiptRoot,text=bus[1],bg="white",fg="red",font=("Source Serif Pro Light",11)).place(x=90,y=60)


           name = Label(receiptRoot,text="Name :",bg="white",font=("Source Serif Pro Light",11)).place(x=30,y=100)
           nameValue = Label(receiptRoot,text=personDetails[0],fg="green",bg="white",font=("Source Serif Pro Light",11)).place(x=90,y=100)

           gender = Label(receiptRoot,text="Gender :",bg="white",font=("Source Serif Pro Light",11)).place(x=200,y=100)
           genderValue = Label(receiptRoot,text=personDetails[1],fg="green",bg="white",font=("Source Serif Pro Light",11)).place(x=270,y=100)

           contact = Label(receiptRoot,text="Contact :",bg="white",font=("Source Serif Pro Light",11)).place(x=30,y=130)
           contactValue = Label(receiptRoot,text=personDetails[2],fg="green",bg="white",font=("Source Serif Pro Light",11)).place(x=100,y=130)

           age = Label(receiptRoot,text="Age :",bg="white",font=("Source Serif Pro Light",11)).place(x=200,y=130)
           ageValue = Label(receiptRoot,text=personDetails[3],fg="green",bg="white",font=("Source Serif Pro Light",11)).place(x=270,y=130)

           From  = Label(receiptRoot,text="From :",bg="white",font=("Source Serif Pro Light",11)).place(x=30,y=180)
           fromValue = Label(receiptRoot,text=journy[2],fg="green",bg="white",font=("Source Serif Pro Light",11)).place(x=80,y=180)


           to  = Label(receiptRoot,text="To :",bg="white",font=("Source Serif Pro Light",11)).place(x=30,y=210)
           toValue = Label(receiptRoot,text=journy[3],fg="green",bg="white",font=("Source Serif Pro Light",11)).place(x=80,y=210)

           date = Label(receiptRoot,text="Date :",bg="white",font=("Source Serif Pro Light",11)).place(x=30,y=235)
           dateValue = Label(receiptRoot,text=journy[0],fg="green",bg="white",font=("Source Serif Pro Light",11)).place(x=80,y=235)

           ticketno = Label(receiptRoot,text="Ticket No :",bg="white",font=("Source Serif Pro Light",11)).place(x=30,y=262)
           ticketnoValue = Label(receiptRoot,text=ticketNo,fg="green",bg="white",font=("Source Serif Pro Light",11)).place(x=110,y=262)

           seatno = Label(receiptRoot,text="Seat No :",bg="white",font=("Source Serif Pro Light",11)).place(x=30,y=290)
           seatnoValue = Label(receiptRoot,text=seatNo,fg="green",bg="white",font=("Source Serif Pro Light",11)).place(x=110,y=290)

           seattype = Label(receiptRoot,text="Type :",bg="white",font=("Source Serif Pro Light",11)).place(x=200,y=290)
           seatValue = Label(receiptRoot,text=bus[2],fg="green",bg="white",font=("Source Serif Pro Light",11)).place(x=250,y=290)

           price = Label(receiptRoot,text="Price :",bg="white",font=("Source Serif Pro Light",11)).place(x=30,y=330)
           priceValue = Label(receiptRoot,text=Price,fg="red",bg="white smoke",font=("Source Serif Pro Light",12)).place(x=100,y=326,width=100)
           bottomframe = Button(receiptRoot,text="close",bg="brown3",fg="white",font=("Arial Black",12),command=lambda : closefunction(receiptRoot,root,ticketNo,seatNo,bus[2],Price,bus[0],personDetails))
           bottomframe.place(x=120,y=450,width=100,height=40)



           receiptRoot.mainloop()






#fillup form function ----------------------------------------------------------


def formfunction(bus,journy,root1) :
       # global root
       root1.destroy()

       root = Tk()
       root.geometry("1000x700+100+0")
       root.resizable(0,0)

       name = StringVar()
       age = IntVar()
       z = IntVar()           #for gender variable parameter
       contact = IntVar()
       # print(str(z[0]))

       formBody = Frame(root,bg="white").place(width=580,height=550,x=60,y=40)

       formHead =  Label(formBody,bg="white",text="Please Enter Details Below",font=("Source Serif Pro Semibold",16),fg="green").place(x=200,y=60)

       nameLabel = Label(formBody,text="Name",font=("sans",14),bg="white").place(x=80,y=150)
       nameEntry = Entry(formBody,font=("sans",12),width=26,textvariable=name).place(x=170,y=150)
#
       ageLabel = Label(formBody,text="Age",font=("sans",14),bg="white").place(x=80,y=190)
       ageEntry = Entry(formBody,font=("sans",12),width=10,textvariable=age).place(x=170,y=190)
#
       contactLabel = Label(formBody,text="Contact",font=("sans",14),bg="white").place(x=80,y=230)
       contactLabe2 = Label(formBody,text="+91",font=("sans",12),width=2,bg="white",fg="green").place(x=170,y=230)
       contactEntry = Entry(formBody,font=("sans",12),textvariable=contact).place(x=200,y=230)
#
       genderLabel = Label(formBody,text="Gender",font=("sans",14),bg="white").place(x=80,y=270)
       male = Radiobutton(formBody,text="Male",font=("sans",12),bg="white",value=1,variable=z).place(x=170,y=270)
       female = Radiobutton(formBody,text="Female",font=("sans",12),bg="white",value=2,variable=z).place(x=270,y=270)
      #-------------------------------------------------------------------

       busdetails = Frame(formBody,bg="white smoke").place(width=520,height=190,x=80,y=330)

       busnoLabel = Label(formBody,text="Bus No :",font=("Source Code Pro Light",11)).place(x=85,y=350)
       busno = Label(formBody,text=bus[0],font=("Source Serif Pro Light",12),fg="green").place(x=165,y=350)

       dateLabel = Label(formBody,text="Date :",font=("Source Serif Pro Light",11)).place(x=250,y=350)
       date = Label(formBody,text=journy[0],font=("Source Serif Pro Light",12),fg="green",width=10).place(x=300,y=350)

       timeLabel = Label(formBody,text="Time :",font=("Source Serif Pro Light",11)).place(x=425,y=350)
       time = Label(formBody,text=journy[1],font=("Source Serif Pro Light",12),fg="green",width=10).place(x=475,y=350)

       boardingLabel = Label(formBody,text="From :",font=("Source Serif Pro Light",11)).place(x=85,y=390)
       boarding = Label(formBody,text=journy[2],font=("Source Serif Pro Light",11),fg="green",width=18).place(x=135,y=390)

       destinationLabel = Label(formBody,text="To :",font=("Source Serif Pro Light",11)).place(x=300,y=390)
       destination = Label(formBody,text=journy[3],font=("Source Serif Pro Light",12),fg="green",width=18).place(x=330,y=390)


       submitButton = Button(formBody,text="Submit",font=("sans",14),bg="green",width=15,fg="white",command=lambda : receiptcall(submitButton,name,age,z,contact,root,bus,journy))
       submitButton.place(x=80,y=540)

       root.mainloop()




#----------------------------------------------------------------------------------------------------




#after clicking on book bus button all details of bus is passed to formfuntion from here-------------

def eventhandlar(x,root1):

    if x == 1 :
        cur.execute('select * from bus_detail where bus_no=101')
        y=cur.fetchone()
        cur.execute('select * from journy_detail where bus_no=101')
        journy=cur.fetchone()

    elif x==2:
        cur.execute("select * from bus_detail where bus_no=202")
        y=cur.fetchone()
        cur.execute('select * from journy_detail where bus_no=202')
        journy=cur.fetchone()

    elif x==3 :
        cur.execute("select * from bus_detail where bus_no=303")
        y=cur.fetchone()
        cur.execute('select * from journy_detail where bus_no=303')
        journy=cur.fetchone()

    elif x==4 :
        cur.execute("select * from bus_detail where bus_no=404")
        y=cur.fetchone()
        cur.execute('select * from journy_detail where bus_no=404')
        journy=cur.fetchone()

    elif x==5 :
        cur.execute("select * from bus_detail where bus_no=505")
        y=cur.fetchone()
        cur.execute('select * from journy_detail where bus_no=505')
        journy=cur.fetchone()

    elif x==6 :
        cur.execute("select * from bus_detail where bus_no=606")
        y=cur.fetchone()
        cur.execute('select * from journy_detail where bus_no=606')
        journy=cur.fetchone()


    formfunction(y,journy,root1)



#-------------------------------------------------------------------------------

#list of bus from where user can select and book ticket_________________________

def buslist_fun():

            root1 = Tk()
            root1.geometry("900x650+160+20")
            root1.resizable(0,0)
            Arrowicon = ImageTk.PhotoImage(file="arrow.png")
            backArraow = ImageTk.PhotoImage(file="backbuttonarrow.png")

            head = Frame(root1,bg="white").place(x=20,y=5,width=860,height=50)
            framebody = Frame(root1,bg="white").place(x=20,y=70,width=860,height=530)
            backButton = Button(head,bg="white",image=backArraow,bd=0,command=lambda : homepage(root1)).place(x=25,y=7,width=45,height=45)


            bus1 = Frame(framebody,bg="white smoke").place(x=40,y=90,width=700,height=65)
            bus1Btn = Button(framebody,text="Book Bus",bg="green",fg="white",font=("Times New Roman",13),command= lambda : eventhandlar(1,root1) ).place(x=750,y=90,width=110,height=65)

            bus1_no = Label(bus1,text="101",font=("Source Serif Pro Semibold",11),bg="dodger blue2",fg="white").place(x=270,y=100)
            bus1_name = Label(bus1,text="Bhanupratap Travels",font=("sans serif pro light",11)).place(x=270,y=130)
            bus1_date = Label(bus1,text="16 jul 22",font=("Source Serif Pro Semibold",10),bg="lime green",fg="white").place(x=450,y=100)
            bus1_boarding = Label(bus1,text="Delhi",font=("Source Serif Pro Semibold",10),fg="navy blue").place(x=450,y=130)
            bus1_Arrow = Label(bus1,image=Arrowicon).place(x=580,y=125,width=30,height=30)
            bus1_destination = Label(bus1,text="Amritsar",font=("Source Serif Pro Semibold",10),fg="red").place(x=630,y=130)
            bus1_type = Label(bus1,text="Non Ac",font=("Source Serif Pro Semibold",10),bg="purple3",fg="white").place(x=650,y=100)
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

            bus2 = Frame(framebody,bg="white smoke").place(x=40,y=170,width=700,height=65)
            bus2Btn = Button(framebody,text="Book Bus",bg="green",fg="white",font=("Times New Roman",13),command= lambda : eventhandlar(2,root1) ).place(x=750,y=170,width=110,height=65)

            bus2_no = Label(bus1,text="202",font=("Source Serif Pro Semibold",11),bg="dodger blue2",fg="white").place(x=270,y=180)
            bus2_name = Label(bus1,text="Hans Travels",font=("sans serif pro light",11)).place(x=270,y=210)
            bus2_date = Label(bus1,text="25 jul 22",font=("Source Serif Pro Semibold",10),bg="lime green",fg="white").place(x=450,y=180)
            bus2_boarding = Label(bus1,text="Chennai",font=("Source Serif Pro Semibold",10),fg="navy blue").place(x=450,y=210)
            bus2_Arrow = Label(bus1,image=Arrowicon).place(x=580,y=205,width=30,height=30)
            bus2_destination = Label(bus1,text="Pune",font=("Source Serif Pro Semibold",10),fg="red").place(x=630,y=210)
            bus2_type = Label(bus1,text="Ac",font=("Source Serif Pro Semibold",10),bg="chocolate1",fg="white",width=5).place(x=655,y=180)
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

            bus3 = Frame(framebody,bg="white smoke").place(x=40,y=250,width=700,height=65)
            bus3Btn = Button(framebody,text="Book Bus",bg="green",fg="white",font=("Times New Roman",13),command= lambda : eventhandlar(3,root1) ).place(x=750,y=250,width=110,height=65)

            bus3_no = Label(bus1,text="303",font=("Source Serif Pro Semibold",11),bg="dodger blue2",fg="white").place(x=270,y=260)
            bus3_name = Label(bus1,text="VRL Travels",font=("sans serif pro light",11)).place(x=270,y=290)
            bus3_date = Label(bus1,text="10 jun 22",font=("Source Serif Pro Semibold",10),bg="lime green",fg="white").place(x=450,y=260)
            bus3_boarding = Label(bus1,text="Kolkata",font=("Source Serif Pro Semibold",10),fg="navy blue").place(x=450,y=290)
            bus3_Arrow = Label(bus1,image=Arrowicon).place(x=580,y=285,width=30,height=30)
            bus3_destination = Label(bus1,text="Patna",font=("Source Serif Pro Semibold",10),fg="red").place(x=630,y=290)
            bus3_type = Label(bus1,text="Non Ac",font=("Source Serif Pro Semibold",10),bg="purple3",fg="white",width=5).place(x=655,y=260)
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

            bus4 = Frame(framebody,bg="white smoke").place(x=40,y=330,width=700,height=65)
            bus4Btn = Button(framebody,text="Book Bus",bg="green",fg="white",font=("Times New Roman",13),command= lambda : eventhandlar(4,root1) ).place(x=750,y=330,width=110,height=65)


            bus4_no = Label(bus1,text="404",font=("Source Serif Pro Semibold",11),bg="dodger blue2",fg="white").place(x=270,y=340)
            bus4_name = Label(bus1,text="Marvel Travels",font=("sans serif pro light",11)).place(x=270,y=370)
            bus4_date = Label(bus1,text="04 jul 22",font=("Source Serif Pro Semibold",10),bg="lime green",fg="white").place(x=450,y=340)
            bus4_boarding = Label(bus1,text="Jaipur",font=("Source Serif Pro Semibold",10),fg="navy blue").place(x=450,y=370)
            bus4_Arrow = Label(bus1,image=Arrowicon).place(x=580,y=365,width=30,height=30)
            bus4_destination = Label(bus1,text="Gandhinagar",font=("Source Serif Pro Semibold",10),fg="red").place(x=630,y=370)
            bus4_type = Label(bus1,text="Ac",font=("Source Serif Pro Semibold",10),bg="chocolate1",fg="white",width=5).place(x=655,y=340)
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

            bus5 = Frame(framebody,bg="white smoke").place(x=40,y=410,width=700,height=65)
            bus5Btn = Button(framebody,text="Book Bus",bg="green",fg="white",font=("Times New Roman",13),command= lambda : eventhandlar(5,root1) ).place(x=750,y=410,width=110,height=65)


            bus5_no = Label(bus1,text="505",font=("Source Serif Pro Semibold",11),bg="dodger blue2",fg="white").place(x=270,y=420)
            bus5_name = Label(bus1,text="SRS Travels",font=("sans serif pro light",11)).place(x=270,y=450)
            bus5_date = Label(bus1,text="02 Aug 22",font=("Source Serif Pro Semibold",10),bg="lime green",fg="white").place(x=450,y=420)
            bus5_boarding = Label(bus1,text="Bangalore",font=("Source Serif Pro Semibold",10),fg="navy blue").place(x=450,y=450)
            bus5_Arrow = Label(bus1,image=Arrowicon).place(x=580,y=445,width=30,height=30)
            bus5_destination = Label(bus1,text="Hyderabad",font=("Source Serif Pro Semibold",10),fg="red").place(x=630,y=450)
            bus5_type = Label(bus1,text="Ac",font=("Source Serif Pro Semibold",10),bg="chocolate1",fg="white",width=5).place(x=655,y=420)
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

            bus6 = Frame(framebody,bg="white smoke").place(x=40,y=490,width=700,height=65)
            bus6Btn = Button(framebody,text="Book Bus",bg="green",fg="white",font=("Times New Roman",13),command= lambda : eventhandlar(6,root1) ).place(x=750,y=490,width=110,height=65)

            bus6_no = Label(bus1,text="606",font=("Source Serif Pro Semibold",11),bg="dodger blue2",fg="white").place(x=270,y=500)
            bus6_name = Label(bus1,text="Srinath Travels",font=("sans serif pro light",11)).place(x=270,y=530)
            bus6_date = Label(bus1,text="26 jul 22",font=("Source Serif Pro Semibold",10),bg="lime green",fg="white").place(x=450,y=500)
            bus6_boarding = Label(bus1,text="Lucknow",font=("Source Serif Pro Semibold",10),fg="navy blue").place(x=450,y=530)
            bus6_Arrow = Label(bus1,image=Arrowicon).place(x=580,y=525,width=30,height=30)
            bus6_destination = Label(bus1,text="gurugram",font=("Source Serif Pro Semibold",10),fg="red").place(x=630,y=530)
            bus6_type = Label(bus1,text="Non Ac",font=("Source Serif Pro Semibold",10),bg="purple3",fg="white",width=5).place(x=655,y=500)


            root1.mainloop()


# buslist_fun()





#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------



# con = co.connect("bus_management/bus")
# cur = con.cursor()






#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

#closing the popup passenger detail window
def close_PassangerDetail_window(rootP,searchButton):
        searchButton['state']='normal'
        searchButton['bg']='green'
        rootP.destroy()
#-------------------------------------------------------------------------------

#extracting passenger data from database to show passenger details--------------

def fetch_data(id):

        Id = id.get()
        print(Id)

        sqlcmd_1 = "select * from passenger_detail where passenger_id = :id"
        cur.execute(sqlcmd_1,id=Id)
        passengerDetail=cur.fetchone()

        ticketNo = passengerDetail[6]
        print(ticketNo)
        sqlcmd2 = "select * from ticket_detail where ticket_no = :Tno"
        cur.execute(sqlcmd2,Tno=ticketNo)
        ticketDetail=cur.fetchone()
        #
        busNo = passengerDetail[5]
        sqlcmd_3 = "select * from bus_detail where bus_no = :Bno"
        cur.execute(sqlcmd_3,Bno=busNo)
        busDetail=cur.fetchone()

        sqlcmd_4 = "select * from journy_detail where bus_no = :Bno"
        cur.execute(sqlcmd_4,Bno=busNo)
        journyDeatil=cur.fetchone()
        #
        # print(journyDeatil)
        #
        return passengerDetail,busDetail[0:3],journyDeatil[0:4],ticketDetail


#-------------------------------------------------------------------------------
# passenger detail window poped up  ----------------------------------

def searchfun(id,root3,searchButton):

    try:
        if id=='':
            raise TypeError

        searchButton['state']='disable'
        searchButton['bg']='red'

        passenger_Detail = fetch_data(id)
        print(passenger_Detail)
        rootP = Toplevel()
        rootP.geometry("420x350+302+240")
        rootP.resizable(0,0)
        date1 = str(passenger_Detail[2][0])
        date2 = date1.split()
        date3 = date2[0]
        detailhead = Frame(rootP,bg="white").place(x=10,y=10,width=400,height=330)


        if passenger_Detail[0][3]=='M':
                profileicon = ImageTk.PhotoImage(file="male.png")
        elif passenger_Detail[0][3]=='F':
                profileicon = ImageTk.PhotoImage(file="female.png")

        profilelogo = Label(rootP,image=profileicon,bg="white",text="hello").place(x=15,y=10,width=90,heigh=90)
        ##
        pessengername = Label(rootP,text=passenger_Detail[0][1],bg="white",font=("Times New Roman",13)).place(x=107,y=30)
        pessengerId = Label(rootP,text=passenger_Detail[0][0],bg="white",font=("DejaVu Sans",13),fg="green").place(x=107,y=55)
        tNo = Label(rootP,text="Ticket No",bg="white",font=("Times New Roman",12)).place(x=240,y=30)
        tNovalue = Label(rootP,text=passenger_Detail[0][6],bg="white",fg="green",font=("DejaVu Sans",10)).place(x=320,y=33)
        Date = Label(rootP,text=date3,bg="white",font=("DejaVu Sans",11),fg="red").place(x=240,y=55)
        # #
        profileBody = Frame(rootP,bg="lavender").place(x=15,y=120,width=385,height=210)
        busNo = Label(rootP,text="Bus No -",bg="lavender",font=("DejaVu Sans",11)).place(x=20,y=135)
        busValue = Label(rootP,text=passenger_Detail[0][5],fg="green",bg="lavender",font=("DejaVu Sans",10)).place(x=100,y=135)
        # #
        busnameValue = Label(rootP,text=passenger_Detail[1][1],fg="green",bg="lavender",font=("DejaVu Sans",10)).place(x=200,y=135)
        # #
        board = Label(rootP,text="From -",bg="lavender",font=("DejaVu Sans",11)).place(x=20,y=170)
        busValue = Label(rootP,text=passenger_Detail[2][2],fg="green",bg="lavender",font=("DejaVu Sans",10)).place(x=100,y=170)
        # #
        destination = Label(rootP,text="To -",bg="lavender",font=("DejaVu Sans",11)).place(x=20,y=205)
        destinationvalue = Label(rootP,text=passenger_Detail[2][3],fg="green",bg="lavender",font=("DejaVu Sans",10)).place(x=100,y=205)
        # #
        seatNo = Label(rootP,text="Seat no -",bg="lavender",font=("DejaVu Sans",11)).place(x=20,y=240)
        seatNovalue = Label(rootP,text=passenger_Detail[3][1],fg="green",bg="lavender",font=("DejaVu Sans",10)).place(x=100,y=240)
        seatType = Label(rootP,text="Seat type -",bg="lavender",font=("DejaVu Sans",11)).place(x=210,y=240)
        seattypeValue = Label(rootP,text=passenger_Detail[1][2],fg="green",bg="lavender",font=("DejaVu Sans",10)).place(x=300,y=240)
        # #
        closeButton = Button(rootP,text="Close",fg="white",bg="brown3",font=("Arial Black",11),command = lambda : close_PassangerDetail_window(rootP,searchButton)).place(x=20,y=280,width=100,height=35)

        rootP.mainloop()

    except TypeError:
        m1=messagebox.showerror('error','invalid passenger ID')
        searchButton['state']='active'
        searchButton['bg']='green'


#passenger id-------------------------------------

# 58ab5
# a4827
# df63c
# 5d199
# 43e45
#-------------------------------------------------------------------------------

#seraching the passenger detail usinng there ID---------------------------------

def checkDetail():

        root3 = Tk()
        root3.geometry("680x440+300+150")
        root3.resizable(0,0)

        passenger_id = StringVar()

        header = Label(root3,text="Check your details",fg="green",font=("Source Serif Pro Semibold",17)).place(x=230,y=1)
        backArraow = ImageTk.PhotoImage(file="backbuttonarrow.png")
        backButton = Button(header,bg="white smoke",image=backArraow,bd=0,command=lambda : homepage(root3)).place(x=25,y=7,width=45,height=45)
        frame_1 = Frame(root3,bg="white").place(x=5,y=60,width=420,height=370)
        Idlabel = Label(root3,text="Enter Passenger Id",font=("Source Serif Pro Light",11)).place(x=437,y=45)
        searchEntry = Entry(root3,font=("Sans",14),textvariable = passenger_id).place(x=440,y=80,width=120,height=35)

        icon = ImageTk.PhotoImage(file="searchicon.png")
        searchButton = Button(root3,bg="green",image=icon,command= lambda : searchfun(passenger_id,root3,searchButton))
        searchButton.place(x=570,y=80,width=55,height=35)

        root3.mainloop()


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# numX=uuid.uuid4()       # 4 byte unique key generated
# x=str(numX)
# print(len(x))
# print(numX)


loadingfun()

callloginfun()
