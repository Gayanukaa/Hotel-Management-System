import sqlite3
from tkinter import *
import datetime
from Classes.CenterFunction import center
from Admin_CusUpdate import AdminCusUpdate
from Admin_RoomUpdate import AdminRoomUpdate
from Classes.Admin import Admin
from Classes.Customer import Customer
from Classes.Rooms import Rooms
from Admin_CheckIn import AdminCheckIn

class AdminInterface:
    def __init__(self,root,username):
        self.root = root
        self.root.geometry("1000x600")
        self.root.update()
        self.root.title("Admin Main Page")
        self.root.resizable(False, False)
        center(self.root,1000,600)

        frame1 = Frame(self.root,bg="grey")
        frame1.place(x=0, y=0, width=1200, height=800)

        img =  PhotoImage(file="Images/Backgrounds/Gradient_background_2.png")
        Label(frame1, image=img).place(x=0, y=0,relwidth=1,relheight=1)

        #self.root.iconbitmap("Images/hnet.com-image.ico")  #For MacOS
        #self.root.iconphoto(False, PhotoImage(file = "Images/hnet.com-image.png")) #For Windows

        username = Admin.getAdminName(username)
        textIntro = "Welcome " + username
        Label(self.root,text =textIntro).place(x=80,y=50)
        temp = datetime.datetime.now()
        textDT = "Today's date:  %s.%s.%s" % (str(temp.day).zfill(2), str(temp.month).zfill(2), temp.year)
        textDT = textDT + "   Time now: %s:%s:%s" % (str(temp.hour).zfill(2), str(temp.minute).zfill(2), str(temp.second).zfill(2))
        Label(self.root,text=textDT).place(x=400,y=50)

        frame1 = Frame(self.root)
        frame1.place(x=70, y=140, width=200, height=400)

        Button(frame1,text="Customer",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.openAdmUpdateCusWindow).pack(padx = 10, pady= 20)
        Button(frame1,text="Check In",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.openAdminCheckInWindow).pack(padx = 10, pady= 10)
        Button(frame1,text="Check Out",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold")).pack(padx = 10, pady= 10)
        Button(frame1,text="Rooms",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.openAdmRoomUpdateWindow).pack(padx = 10, pady= 10)
        Button(frame1,text="Reports",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold")).pack(padx = 10, pady= 10)
        Button(frame1,text="Profile",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold")).pack(padx = 10, pady= 10)
        Button(frame1,text="Sign Out",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.signout).pack(padx = 10, pady= 10)

        temp1 = self.getAvailableRooms()
        textAvRooms = "Rooms Available: \n(" + str(temp1) + ")"
        temp2 = Customer.getNoofCustomers()
        textNofCus  = "No. of Customers: \n(" + str(temp2) + ")"
        temp3 = Rooms.getCheckIn()
        textTdChkIn = "Today's Check In: \n(" + str(temp3) + ")"
        Label(self.root,text=textAvRooms).place(x=400,y=150)
        Label(self.root,text=textTdChkIn).place(x=550,y=150)
        Label(self.root,text=textNofCus).place(x=700,y=150)

        self.root.mainloop()

    def openAdmRoomUpdateWindow(self):
        AdminRoomUpdate(self.root)

    def signout(self):
        self.root.destroy()

    def getAvailableRooms(self):
        connection2 = sqlite3.connect("Databases/Hotel_Database.db")
        cursorRm =connection2.cursor()
        data = "RoomNo"
        goal = "Status"
        constrain = "Available"
        cursorRm.execute("select %s from Room_Details where %s=?" % (data, goal), (constrain,))
        valideData = cursorRm.fetchall()
        return len(valideData)

    def openAdmUpdateCusWindow(self):
        AdminCusUpdate(self.root)

    def openAdminCheckInWindow(self):
        AdminCheckIn(self.root)