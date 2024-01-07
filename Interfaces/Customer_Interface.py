import sqlite3
from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import datetime
from Classes.CenterFunction import center
from Classes.Customer import Customer
from Customer_Profile import CustomerProfile
from Customer_BookRoom import CusBookRoom
from Room_Details import RoomDetails
from Customer_Booking_Details import CusBookDetails

class CustomerInterface:
    def __init__(self,root,username):
        self.root = root
        self.root.geometry("1000x600")
        self.root.update()
        self.root.title("Customer Main Page")
        self.root.resizable(False, False)
        self.root.wm_attributes('-transparent')
        center(self.root,1000,600)

        self.adultCount = StringVar()
        self.childCount = StringVar()

        self.img =  PhotoImage(file="Images/Backgrounds/Gradient_background_4.png")
        Label(self.root, image=self.img).place(x=0, y=0,relwidth=1,relheight=1)
        #self.root.iconbitmap("Images/hnet.com-image.ico")  #For MacOS
        #self.root.iconphoto(False, PhotoImage(file = "Images/hnet.com-image.png")) #For Windows

        self.username = username
        customerName = Customer.getCustomerName(self.username)
        textIntro = "Welcome " + customerName
        Label(self.root,text=textIntro,font=('calibre',20,'normal')).place(x=70,y=50)
        temp = datetime.datetime.now()
        textDT = "Today's date:  %s.%s.%s" % (str(temp.day).zfill(2), str(temp.month).zfill(2), temp.year)
        textDT = textDT + "   Time now: %s:%s:%s" % (str(temp.hour).zfill(2), str(temp.minute).zfill(2), str(temp.second).zfill(2))
        Label(self.root,text=textDT,font=('calibre',20,'normal')).place(x=400,y=50)

        frame1 = Frame(self.root,bg="grey")
        frame1.place(x=70, y=140, width=200, height=350)

        Button(frame1,text="Profile",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.openCusProfile).pack(padx = 10, pady= 20)
        Button(frame1,text="Book a Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.openRoomBooking).pack(padx = 10, pady= 15)
        Button(frame1,text="Booking Details",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.openBookingDetails).pack(padx = 10, pady= 15)
        Button(frame1,text="Room Details",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.openRoomDetails).pack(padx = 10, pady= 15)
        Button(frame1,text="Sign Out",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.signout).pack(padx = 10, pady= 15)

        Label(self.root,text ="Check IN").place(x=400,y=150)
        self.checkINdate = StringVar()
        DateEntry(self.root,selectmode='day',textvariable=self.checkINdate).place(x=500,y=150)
        def my_upd1(*args):
            self.checkINdate.set(self.checkINdate.get())
        self.checkINdate.trace('w',my_upd1)
        Label(self.root,text ="No. of Adults").place(x=650,y=150)
        Entry(self.root,textvariable = self.adultCount,font=('calibre',10,'normal')).place(x=750,y=150)

        Label(self.root,text ="Check OUT").place(x=400,y=190)
        self.checkOutdate = StringVar()
        DateEntry(self.root,selectmode='day',textvariable=self.checkOutdate).place(x=500,y=190)
        def my_upd2(*args):
            self.checkOutdate.set(self.checkOutdate.get())
        self.checkOutdate.trace('w',my_upd2)
        Label(self.root,text ="No. of Children").place(x=650,y=190)
        Entry(self.root,textvariable = self.childCount,font=('calibre',10,'normal')).place(x=750,y=190)

        Button(self.root,text="Search",relief=RAISED,command=self.showPossibleRooms).place(x=600,y=230)

        self.imgP =  PhotoImage(file="Images/Hotel_Pool.png")
        Label(self.root, image=self.imgP, highlightthickness=0,borderwidth=0).place(x=340, y=270)

        self.root.mainloop()

    def showPossibleRooms(self):
        inDate = self.checkINdate.get()
        outDate = self.checkOutdate.get()
        noOfAdults = self.adultCount.get()
        noOfChildren = self.childCount.get()
        rooms = []

        if(inDate == None or outDate == None or noOfAdults == '' or noOfChildren == ''):
            msg = "Enter values"
            messagebox.showerror("Error",msg)

        else:
            try:
                noOfChildren = int(noOfChildren)
                noOfAdults = int(noOfAdults)
                connection2 = sqlite3.connect("Databases/Hotel_Database.db")
                cursorRm =connection2.cursor()
                noOfChildren = noOfChildren//2
                total = noOfChildren + noOfAdults
                option = "Capacity"
                cursorRm.execute("select * from Room_Data where %s=?" % (option), (total,))
                bookableRooms = cursorRm.fetchall()
            except sqlite3.Error as error:
                bookableRooms = str(error)
            except IndexError as error:
                bookableRooms = str(error)

            for i in bookableRooms:
                rooms.append(i[0])

            formatted_string = '\n'.join([f'{room} Room at Rs. {price}, base price for {people} people' for room, price, people in bookableRooms])
            msg = "Avaiable rooms for the entered details are\n\n" + formatted_string + "\n\n Please proceed to the booking window."
            messagebox.showinfo(title="Available Rooms",message=msg)

    def openCusProfile(self):
        CustomerProfile(self.root,self.username)

    def openRoomBooking(self):
        CusBookRoom(self.root,self.username)

    def openRoomDetails(self):
        RoomDetails(self.root)

    def openBookingDetails(self):
        CusBookDetails(self.root)

    def signout(self):
        self.root.destroy()