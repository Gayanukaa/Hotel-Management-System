from tkinter import *
import sqlite3
from tkinter import messagebox
from Classes.CenterFunction import center
from Classes.Booking import Booking

class AdminCheckIn:
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.geometry("1000x600")
        self.root.update()
        self.root.title("Admin Check-In Page")
        self.root.resizable(False, False)
        center(self.root, 1000, 600)

        self.img =  PhotoImage(file="Images/Backgrounds/Gradient_background_4.png")
        Label(self.root, image=self.img).place(x=0, y=0,relwidth=1,relheight=1)

        self.dataEntered = StringVar()
        self.bookingID = StringVar
        self.cusname = StringVar()
        self.cuscontactNo = StringVar()
        self.checkIn = StringVar()
        self.checkOut = StringVar()
        self.noOfAdults = StringVar()
        self.noOfChildren = StringVar()
        self.total = StringVar()
        self.roomNo = StringVar()
        self.advance = StringVar()
        self.balance = StringVar()
        self.mealPlan = StringVar()
        self.priceForOne = StringVar()

        Label(self.root,text ="Check-In Details",font=('calibre',25,'normal')).place(x=400,y=30)

        frame = Frame(self.root)
        frame.place(x=270, y=80, width=450, height=45)

        Label(frame,text ="Booking_ID",font=('calibre',15,'normal')).place(x=30,y=9)
        Entry(frame,textvariable = self.dataEntered, font=('calibre',10,'normal')).place(x=160, y=12)
        Button(frame,text="Search",relief=RAISED,command=self.loadCheckInDetails).place(x=350,y=8)

        frame1 = Frame(self.root,bg="grey")
        frame1.place(x=50, y=150, width=900, height=170)

        Label(frame1,text ="Name").place(x=20,y=20)
        Entry(frame1,textvariable = self.cusname, font=('calibre',10,'normal'),state='disabled').place(x=140,y=20)
        Label(frame1,text ="Check IN").place(x=320,y=20)
        Entry(frame1,textvariable = self.checkIn, font=('calibre',10,'normal'),state='disabled').place(x=400,y=20)
        Label(frame1,text ="No. of Adults").place(x=600,y=20)
        Entry(frame1,textvariable = self.noOfAdults, font=('calibre',10,'normal'),state='disabled').place(x=700, y=20)

        Label(frame1,text ="Contact No.").place(x=20,y=70)
        Entry(frame1,textvariable = self.cuscontactNo, font=('calibre',10,'normal'),state='disabled').place(x=140,y=70)
        Label(frame1,text ="Check OUT").place(x=320,y=70)
        Entry(frame1,textvariable = self.checkOut, font=('calibre',10,'normal'),state='disabled').place(x=400,y=70)
        Label(frame1,text ="No. of Childs").place(x=600,y=70)
        Entry(frame1,textvariable = self.noOfChildren, font=('calibre',10,'normal'),state='disabled').place(x=700, y=70)

        Label(frame1,text ="Meal Plan").place(x=20,y=120)
        Entry(frame1,textvariable = self.mealPlan, font=('calibre',10,'normal'),state='disabled').place(x=140,y=120)

        frame2 = Frame(self.root,bg="black")
        frame2.place(x=50, y=350, width=400, height=40)

        Label(frame2,text ="Room ID",fg="white").place(x=20,y=10)
        Entry(frame2, font=('calibre',10,'normal'),state='disabled').place(x=140, y=10)
        Button(frame2,text="Search",relief=RAISED).place(x=300,y=7)

        frame3 = Frame(self.root,bg="grey")
        frame3.place(x=50, y=410, width=900, height=100)

        Label(frame3,text ="Price for One").place(x=20,y=20)
        Entry(frame3,textvariable = self.priceForOne, font=('calibre',10,'normal'),state="disabled").place(x=140, y=20)
        Label(frame3,text ="Total").place(x=320,y=20)
        Entry(frame3,textvariable = self.total, font=('calibre',10,'normal'),state="disabled").place(x=410, y=20)

        Label(frame3,text ="Room No.").place(x=20,y=70)
        Entry(frame3,textvariable = self.roomNo, font=('calibre',10,'normal'),state="disabled").place(x=140, y=70)
        Label(frame3,text ="Advance").place(x=320,y=70)
        Entry(frame3,textvariable = self.advance, font=('calibre',10,'normal'),state='disabled').place(x=410, y=70)
        Label(frame3,text ="Balance").place(x=600,y=70)
        Entry(frame3,textvariable = self.balance, font=('calibre',10,'normal'),state="disabled").place(x=700, y=70)

        Button(self.root,text="CheckIn",relief=RAISED,command=self.checkInCustomer).place(x=350,y=550)
        Button(self.root,text="Update",relief=RAISED).place(x=470,y=550)
        Button(self.root,text="Clear",relief=RAISED,command=self.clearWindow).place(x=570,y=550)

        self.root.mainloop()

    def loadCheckInDetails(self):

        option = "Booking_ID"
        entered = self.dataEntered.get()

        if(option != None or entered != None):
            data = Booking.getBookingDetails(option,entered)

            self.cusname.set(data[0][2])
            self.cuscontactNo.set(data[0][4])
            self.checkIn.set(data[0][5])
            self.checkOut.set(data[0][6])
            self.noOfAdults.set(data[0][7])
            self.noOfChildren.set(data[0][8])
            self.total.set(data[0][13])
            self.roomNo.set(data[0][10])
            self.advance.set(data[0][12])
            self.mealPlan.set(data[0][14])
            self.priceForOne.set(data[0][9])
            self.balance.set(round(float(self.total.get()) - float(self.advance.get()),2))

        else:
            messagebox.showerror("Error","Please enter data to search")

    def clearWindow(self):
        self.dataEntered.set("")
        self.bookingID.set("")
        self.cusname.set("")
        self.cuscontactNo.set("")
        self.checkIn.set("XX.XX.XXXX")
        self.checkOut.set("XX.XX.XXXX")
        self.noOfAdults.set("")
        self.noOfChildren.set("")
        self.total.set("")
        self.roomNo.set("")
        self.advance.set("")
        self.balance.set("")
        self.mealPlan.set("")
        self.priceForOne.set("")

    def checkInCustomer(self):
        print("Customer balance collected")
        try:
            connection2 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorRm =connection2.cursor()
            data = "Status"
            goal = "RoomNo"
            constrain = self.roomNo.get()
            cursorRm.execute("select %s from Room_Details where %s=?" % (data, goal), (constrain,))
            valideData = cursorRm.fetchall()
            status = valideData[0][0]

            if(status == "Booked"):
                sqln = """update Room_Details set Status = ? where RoomNo = ?"""
                data = ["CheckedIn",self.roomNo.get()]
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

            if(status == "Booked"):
                sqln = """update Customer_Data set Status = ? where Name = ?"""
                data = ["CheckedIn",self.cusname.get()]
                cursorCus.execute(sqln,data)
                connection1.commit()
                connection1.close()
                messagebox.showerror("Message","Customer Checked In or not Booked")
                self.root.destroy
            else:
                connection1.close()
                messagebox.showerror("Error","Customer already Checked In")
        except sqlite3.Error as error:
            print(error)
        except IndexError as error:
            print(error)