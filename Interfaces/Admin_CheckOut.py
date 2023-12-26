import datetime
import sqlite3
from tkinter import *
from tkinter import messagebox
from Classes.CenterFunction import center
from Classes.Customer import Customer
from Classes.Booking import Booking

class AdminCheckOut:
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.geometry("1000x600")
        self.root.update()
        self.root.title("Admin CheckOut Page")
        self.root.resizable(False, False)
        center(self.root, 1000, 600)

        self.img =  PhotoImage(file="Images/Backgrounds/Gradient_background_2.png")
        Label(self.root, image=self.img).place(x=0, y=0,relwidth=1,relheight=1)

        self.dataEntered = StringVar()
        self.cusname = StringVar()
        self.contactNo = StringVar()
        self.checkIn = StringVar()
        self.checkOut = StringVar()
        self.total = StringVar()
        self.roomNo = StringVar()
        self.advance = StringVar()
        self.balance = StringVar()

        Label(self.root,text ="Check-Out Details",font=('calibre',25,'normal')).place(x=400,y=30)

        frame1 = Frame(self.root, bg="black")
        frame1.place(x=270, y=80, width=450, height=45)

        Label(frame1,text ="Booking_ID",font=('calibre',15,'normal')).place(x=30,y=9)
        Entry(frame1,textvariable = self.dataEntered, font=('calibre',10,'normal')).place(x=160, y=12)
        Button(frame1,text="Search",relief=RAISED,command=self.loadCheckOutDetails).place(x=350,y=8)

        frame2 = Frame(self.root, bg="black")
        frame2.place(x=100, y=150, width=330, height=420)

        Label(frame2,text ="Name").place(x=20,y=20)
        Entry(frame2,textvariable = self.cusname, font=('calibre',10,'normal'),state="disabled").place(x=140, y=20)

        Label(frame2,text ="Contact No.").place(x=20,y=70)
        Entry(frame2,textvariable = self.contactNo, font=('calibre',10,'normal'),state="disabled").place(x=140, y=70)

        Label(frame2,text ="Room No.").place(x=20,y=120)
        Entry(frame2,textvariable = self.roomNo, font=('calibre',10,'normal'),state="disabled").place(x=140, y=120)

        Label(frame2,text ="Check In").place(x=20,y=170)
        Entry(frame2,textvariable = self.checkIn, font=('calibre',10,'normal'),state="disabled").place(x=140, y=170)

        Label(frame2,text ="Check Out").place(x=20,y=220)
        Entry(frame2,textvariable = self.checkOut, font=('calibre',10,'normal'),state="disabled").place(x=140, y=220)

        Label(frame2,text ="Total Bill").place(x=20,y=270)
        Entry(frame2,textvariable = self.total, font=('calibre',10,'normal'),state="disabled").place(x=140, y=270)

        Label(frame2,text ="Advance").place(x=20,y=320)
        Entry(frame2,textvariable = self.advance, font=('calibre',10,'normal'),state="disabled").place(x=140, y=320)

        Label(frame2,text ="Balance").place(x=20,y=370)
        Entry(frame2,textvariable = self.balance, font=('calibre',10,'normal'),state="disabled").place(x=140, y=370)

        Button(self.root,text="Print",relief=RAISED,command=self.createPrintableForm).place(x=550,y=140)
        Button(self.root,text="CheckOut",relief=RAISED,command=self.checkOutCustomer).place(x=680,y=140)
        Button(self.root,text="Clear",relief=RAISED,command=self.clearWindow).place(x=820,y=140)

        frameP = Frame(self.root, bg="white", width=500, height=400)
        frameP.place(x=470, y=180)

        self.root.mainloop()

    def loadCheckOutDetails(self):
        option = "Booking_ID"
        entered = self.dataEntered.get()

        if(option != None or entered != None):
            data = Booking.getBookingDetails(option,entered)

            self.cusname.set(data[0][2])
            self.contactNo.set(data[0][4])
            self.checkIn.set(data[0][5])
            self.checkOut.set(data[0][6])
            self.total.set(data[0][13])
            self.roomNo.set(data[0][10])
            self.advance.set(data[0][12])
            self.balance.set(round(float(self.total.get()) - float(self.advance.get()),2))
        else:
            messagebox.showerror("Error","Please enter data to search")

    def clearWindow(self):
        self.dataEntered.set("")
        self.cusname.set("")
        self.contactNo.set("")
        self.checkIn.set("XX.XX.XXXX")
        self.checkOut.set("XX.XX.XXXX")
        self.total.set("")
        self.roomNo.set("")
        self.advance.set("")
        self.balance.set("")

    def createPrintableForm(self):
        try:
            connection2 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorRm =connection2.cursor()
            data = "Status"
            goal = "RoomNo"
            constrain = self.roomNo.get()
            cursorRm.execute("select %s from Room_Details where %s=?" % (data, goal), (constrain,))
            valideData = cursorRm.fetchall()
            status = valideData[0][0]

            if(status == "CheckedIn"):
                frameP = Frame(self.root, bg="white", width=500, height=400)
                frameP.place(x=470, y=180)

                self.img1 = PhotoImage(file="Images/Icons/hotel_logo.png")
                Label(frameP, image=self.img1, bg="white").place(x=30, y=10)

                Label(frameP, text="Loren Impsum Hotel", bg="white", fg="black", borderwidth=2, relief="solid",font=('calibre',20,'normal')).place(x=210, y=20)
                Label(frameP, text="Address: Perera Road, Nowhereville\nContactNo: 011 911 9119", bg="white", fg="black", borderwidth=2, relief="solid",font=('calibre',15,'normal')).place(x=170, y=52)

                Label(frameP, text="Issue Date: " + self.checkOut.get(), bg="white", fg="black", relief="solid",font=('calibre',15,'normal')).place(x=30, y=125)
                Label(frameP, text="Customer Details", bg="white", fg="black", relief="solid",font=('calibre',15,'normal')).place(x=30, y=155)

                framePinner = Frame(frameP, bg="white",highlightbackground="grey",highlightthickness=2,width=420, height=150)
                framePinner.place(x=40, y=190)

                Label(framePinner, text="Name: " + self.cusname.get(), bg="white", fg="black", borderwidth=2, relief="solid",font=('calibre',15,'normal')).place(x=20, y=20)
                Label(framePinner, text="Contact No: " + self.contactNo.get(), bg="white", fg="black", borderwidth=2, relief="solid",font=('calibre',15,'normal')).place(x=220, y=20)
                Label(framePinner, text="Check In: " + self.checkIn.get(), bg="white", fg="black", borderwidth=2, relief="solid",font=('calibre',15,'normal')).place(x=20, y=60)
                Label(framePinner, text="Check Out: " + self.checkOut.get(), bg="white", fg="black", borderwidth=2, relief="solid",font=('calibre',15,'normal')).place(x=220, y=60)
                Label(framePinner, text="Room No: " + self.roomNo.get(), bg="white", fg="black", borderwidth=2, relief="solid",font=('calibre',15,'normal')).place(x=20, y=100)

                date1_str = str(self.checkIn.get())
                date2_str = str(self.checkOut.get())
                date1 = datetime.datetime.strptime(date1_str, "%m/%d/%y")
                date2 = datetime.datetime.strptime(date2_str, "%m/%d/%y")

                difference = date2 - date1
                total_days = difference.days

                Label(framePinner, text="No. of Days: " + str(total_days), bg="white", fg="black", relief="solid",font=('calibre',15,'normal')).place(x=220, y=100)

                Label(frameP, text="Total: ", bg="white", fg="red", relief="solid",font=('calibre',20,'normal')).place(x=50, y=360)
                Label(frameP, text=self.total.get(), bg="grey", fg="black", relief="solid",font=('calibre',20,'normal')).place(x=350, y=360)
            else:
                frameP = Frame(self.root, bg="white", width=500, height=400)
                frameP.place(x=470, y=180)
        except sqlite3.Error as error:
            print(error)
        except IndexError as error:
            print(error)

    def checkOutCustomer(self):
        try:
            connection2 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorRm =connection2.cursor()
            data = "Status"
            goal = "RoomNo"
            constrain = self.roomNo.get()
            cursorRm.execute("select %s from Room_Details where %s=?" % (data, goal), (constrain,))
            valideData = cursorRm.fetchall()
            status = valideData[0][0]

            if(status == "CheckedIn"):
                sqln = """update Room_Details set Status = ? where RoomNo = ?"""
                data = ["Available",self.roomNo.get()]
                cursorRm.execute(sqln,data)
                connection2.commit()
                connection2.close()
                self.root.destroy
            else:
                connection2.close()
                messagebox.showerror("Error","Room already in Use or not Booked")
        except sqlite3.Error as error:
            print(error)
        except IndexError as error:
            print(error)

        try:
            connection1 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorCus =connection1.cursor()
            data = "Status"
            goal = "Name"
            constrain = self.cusname.get()
            cursorCus.execute("select %s from Customer_Data where %s=?" % (data, goal), (constrain,))
            valideData = cursorCus.fetchall()
            status = valideData[0][0]

            if(status == "CheckedIn"):
                sqln = """update Customer_Data set Status = ? where Name = ?"""
                data = ["Registered",self.cusname.get()]
                cursorCus.execute(sqln,data)
                connection1.commit()
                connection1.close()
                messagebox.showerror("Message","Customer Checked Out")
                self.root.destroy
            else:
                connection1.close()
                messagebox.showerror("Error","Customer already Checked In")
        except sqlite3.Error as error:
            print(error)
        except IndexError as error:
            print(error)