from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from Classes.CenterFunction import center
from Classes.Customer import Customer
from Classes.Booking import Booking

class CusBookRoom:
    def __init__(self,root,username):
        self.root = Toplevel(root)
        self.root.geometry("1000x600")
        self.root.update()
        self.root.title("Room Booking Page")
        self.root.resizable(False, False)
        center(self.root,1000,600)

        img =  PhotoImage(file="Images/Backgrounds/Gradient_background_10.png")
        Label(self.root, image=img).place(x=0, y=0,relwidth=1,relheight=1)

        #self.root.iconbitmap("Images/hnet.com-image.ico")  #For MacOS
        #self.root.iconphoto(False, PhotoImage(file = "Images/hnet.com-image.png")) #For Windows

        self.checkINdate = StringVar()
        self.checkOutdate = StringVar()
        self.adultCount = StringVar()
        self.childCount = StringVar()
        self.childAges = StringVar()
        self.mealPlan = StringVar()
        self.additionalPrice = StringVar()
        self.cusname= StringVar()
        self.cuscontactNo = StringVar()
        self.roomID = StringVar()
        self.price = StringVar()
        self.roomNo = StringVar()
        self.total = StringVar()
        self.advance = StringVar()
        self.balance = StringVar()
        self.advanceLocal = None
        self.balanceLocal = None

        self.username = username
        option = "Username"
        entered = self.username

        if(option != None or entered != None):
            data = Customer.getData(option,entered)
            self.cusname.set(data[0][1])
            self.cuscontactNo.set(data[0][5])
        else:
            messagebox.showerror("Error","No data found")


        Label(self.root,text ="Book Room",font=('calibre',20,'normal')).place(x=450,y=50)
        
        frame1 = Frame(self.root,bg="grey")
        frame1.place(x=50, y=100, width=900, height=170)

        Label(frame1,text ="Name").place(x=20,y=20)
        Entry(frame1,textvariable = self.cusname, font=('calibre',10,'normal')).place(x=140,y=20)
        Label(frame1,text ="Check IN").place(x=320,y=20)
        DateEntry(frame1,selectmode='day',textvariable=self.checkINdate).place(x=410,y=20)
        def my_upd1(*args):
            self.checkINdate.set(self.checkINdate.get())
        self.checkINdate.trace('w',my_upd1)
        Label(frame1,text ="No. of Adults").place(x=600,y=20)
        Entry(frame1,textvariable = self.adultCount, font=('calibre',10,'normal')).place(x=700, y=20)

        Label(frame1,text ="Contact No.").place(x=20,y=70)
        Entry(frame1,textvariable = self.cuscontactNo, font=('calibre',10,'normal')).place(x=140,y=70)
        Label(frame1,text ="Check OUT").place(x=320,y=70)
        DateEntry(frame1,selectmode='day',textvariable=self.checkOutdate).place(x=410,y=70)
        def my_upd1(*args):
            self.checkOutdate.set(self.checkOutdate.get())
        self.checkOutdate.trace('w',my_upd1)
        Label(frame1,text ="No. of Childs").place(x=600,y=70)
        Entry(frame1,textvariable = self.childCount, font=('calibre',10,'normal')).place(x=700, y=70)

        Label(frame1,text ="Meal Plan").place(x=20,y=120)
        mealOp = ["Room Only","Bed and Breakfast","Half Board","Full Board","All Inclusive"] # Dropdown menu options
        self.mealPlan.set("Room Only") # initial menu text
        OptionMenu(frame1,self.mealPlan ,*mealOp ).place(x=140,y=120) # Create Dropdown menu
        Entry(frame1, textvariable = self.additionalPrice, font=('calibre',10,'normal'),state='readonly').place(x=320, y=120)
        self.additionalPrice.set("Type")
        Label(frame1,text ="Child Ages").place(x=600,y=120)
        Entry(frame1,textvariable = self.childAges, font=('calibre',10,'normal')).place(x=700, y=120)
        self.childAges.set("Ages under 12 - Enter as X,X,")

        frame2 = Frame(self.root,bg="black")
        frame2.place(x=50, y=300, width=400, height=40)

        Label(frame2,text ="Room ID",fg="white").place(x=20,y=10)
        Entry(frame2,textvariable = self.roomID, font=('calibre',10,'normal'),state='readonly').place(x=100, y=10)
        Button(frame2,text="Search",relief=RAISED,command=self.searchRoom).place(x=280,y=7)

        frame3 = Frame(self.root,bg="grey")
        frame3.place(x=50, y=380, width=900, height=100)

        Label(frame3,text ="Price").place(x=20,y=20)
        Entry(frame3,textvariable = self.price, font=('calibre',10,'normal'),state="disabled").place(x=140, y=20)
        Label(frame3,text ="Total").place(x=320,y=20)
        Entry(frame3,textvariable = self.total, font=('calibre',10,'normal'),state="disabled").place(x=410, y=20)

        Label(frame3,text ="Room No.").place(x=20,y=70)
        Entry(frame3,textvariable = self.roomNo, font=('calibre',10,'normal'),state="disabled").place(x=140, y=70)
        Label(frame3,text ="Advance").place(x=320,y=70)
        Entry(frame3,textvariable = self.advance, font=('calibre',10,'normal')).place(x=410, y=70)
        Label(frame3,text ="Balance").place(x=600,y=70)
        Entry(frame3,textvariable = self.balance, font=('calibre',10,'normal'),state="disabled").place(x=700, y=70)

        Button(self.root,text="Confirm",relief=RAISED,command=self.calculateBookings).place(x=350,y=540)
        Button(self.root,text="Book",relief=RAISED,command=self.createBooking).place(x=470,y=540)
        Button(self.root,text="Clear",relief=RAISED,command=self.clearWindow).place(x=570,y=540)

        self.root.mainloop()
    
    def searchRoom(self):
        checkIn = self.checkINdate.get()
        checkOut = self.checkOutdate.get()
        noOfAdults = self.adultCount.get()
        noOfChildren = self.childCount.get()
        childAges = self.childAges.get()

        mealPlan = self.mealPlan.get()
        match(mealPlan):
            case "Room Only": self.additionalPrice.set(None)
            case "Bed and Breakfast": self.additionalPrice.set("24 hours room/breakfast")
            case "Half Board": self.additionalPrice.set("24 hours room/breakfast & lunch")
            case "Full Board": self.additionalPrice.set("24 hours / 3 meals")
            case "All Inclusive": self.additionalPrice.set("24 hours room/ 3 meals/other")
            case _: self.additionalPrice.set("None")

        status = (Booking.compareDates(checkIn,checkOut)) 
        
        if (childAges == "Ages under 12 - Enter as X,X," or childAges == 0 or childAges == '-'):
            childAges = None
        else:
            try:
                childAges = childAges.split(",")
                childAges = [int(i) for i in childAges]
                if(len(childAges) < int(noOfChildren)):
                    messagebox.showerror("Error","Enter all child ages")
                    return None
                elif(len(childAges) > int(noOfChildren)):
                    messagebox.showerror("Error","Remove unnecessary child ages")
                    return None
            except ValueError:
                messagebox.showerror("Error","Enter child ages correctly using comma")
                return None

        if(status == True):
            roomDetails = Booking.findRoom(checkIn,checkOut,noOfAdults,noOfChildren,mealPlan,childAges)
            if(roomDetails != None):
                self.roomID.set(roomDetails[0])
                self.price.set(roomDetails[1])
                self.total.set(roomDetails[2])
                self.roomNo.set(roomDetails[3])
                self.advance.set("Enter - Minimum(" + str(roomDetails[4]) + ")")
                self.advanceLocal = roomDetails[4]

            else:
                messagebox.showerror("Error","No rooms available")
        else:
            messagebox.showerror("Error","Check IN date should be before Check OUT date")
            return None

    def calculateBookings(self):
        advance = self.advance.get()
        if(advance == "" or advance == None):
            messagebox.showerror("Error","Enter advance")
            return None
        else:
            try:
                advance = int(advance)
                if(advance < self.advanceLocal):
                    messagebox.showerror("Error","Enter advance - Minimum(" + str(self.advanceLocal) + ")")
                    return None
                else:
                    self.balanceLocal = int(self.total.get()) - advance
                    self.balance.set(self.balanceLocal)
            except ValueError:
                messagebox.showerror("Error","Enter advance correctly")
                return None

    def createBooking(self):
        pass

    def clearWindow(self):  
        self.checkINdate.set("")
        self.checkOutdate.set("")      
        self.adultCount.set("")
        self.childCount.set("")
        self.childAges.set("Ages under 12 - Enter as X,X,")
        self.mealPlan.set("Room Only")
        self.additionalPrice.set("Type")
        self.roomID.set("")
        self.price.set("")
        self.roomNo.set("")
        self.total.set("")
        self.advance.set("")
        self.balance.set("")
        self.advanceLocal = None
        self.balanceLocal = None