from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from Classes.CenterFunction import center
from Classes.Customer import Customer

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

        self.username = username
        option = "Username"
        entered = self.username

        if(option != None or entered != None):
            data = Customer.getData(option,entered)
            self.cusname = data[0][1]
            self.cuscontactNo = data[0][5]
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
        mealOp = ["Room Only","Bed & Breakfast","Half Board","Full Board","All Inclusive"] # Dropdown menu options
        self.mealPlan.set("Room Only") # initial menu text
        OptionMenu(frame1,self.mealPlan ,*mealOp ).place(x=140,y=120) # Create Dropdown menu
        Entry(frame1, textvariable = self.additionalPrice, font=('calibre',10,'normal')).place(x=320, y=120)
        self.additionalPrice.set("Additional Price")
        Label(frame1,text ="Child Ages").place(x=600,y=120)
        Entry(frame1,textvariable = self.childAges, font=('calibre',10,'normal')).place(x=700, y=120)
        self.childAges.set("Enter as X,X,X")

        frame2 = Frame(self.root,bg="black")
        frame2.place(x=50, y=300, width=400, height=40)

        Label(frame2,text ="Room ID",fg="white").place(x=20,y=10)
        Entry(frame2,textvariable = self.roomID, font=('calibre',10,'normal')).place(x=100, y=10)
        Button(frame2,text="Search",relief=RAISED).place(x=280,y=7)

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

        Button(self.root,text="Confirm",relief=RAISED).place(x=350,y=540)
        Button(self.root,text="Book",relief=RAISED).place(x=470,y=540)
        Button(self.root,text="CLEAR",relief=RAISED).place(x=550,y=540)

        self.root.mainloop()
    
    """ def searchData(self):
        option = self.clickedOption.get()
        entered = self.dataEntered.get()

        if(option != None or entered != None):
            data = Customer.getData(option,entered)
            
            self.cuscustomerID.set(data[0][0])
            self.cusname.set(data[0][1])
            self.clickedTitle.set(data[0][2])
            self.cusdob.set(data[0][3])
            self.clickedGen.set(data[0][4])
            self.cuscontactNo.set(data[0][5])
            self.cusidNo.set(data[0][6])
            self.cusemail.set(data[0][7])
            self.cusnationality.set(data[0][8])
            self.cusaddress.set(data[0][9])
        else:
            messagebox.showerror("Error","Please enter data to search")

    def sendCusData(self):
        customer = Customer()
        customer.name = self.cusname.get()
        customer.title = self.clickedTitle.get()
        customer.dob = self.cusdob.get()
        customer.gender = self.clickedGen.get()
        customer.contactNo = self.cuscontactNo.get()
        customer.idNo = self.cusidNo.get()
        customer.email = self.cusemail.get()
        customer.nationality = self.cusnationality.get()
        customer.address = self.cusaddress.get()
        customer.username = None
        customer.password = None
        
        status = customer.enterDatatoDatabase(customer.name,customer.title,customer.dob,customer.gender,customer.contactNo,customer.idNo,customer.email,customer.nationality,customer.address,customer.username,customer.password)

    def updateCusData(self):
        option = self.clickedOption.get()
        status = True

        if(option == "Customer_ID"):
            name = self.cusname.get()
            title = self.clickedTitle.get()
            dob = self.cusdob.get()
            gender = self.clickedGen.get()
            contactNo = self.cuscontactNo.get()
            idNo = self.cusidNo.get()
            email = self.cusemail.get()
            nationality = self.cusnationality.get()
            address = self.cusaddress.get()
            entered = self.dataEntered.get()

            msg,status = Customer.updateDatatoDatabase(name,title,dob,gender,contactNo,idNo,email,nationality,address,entered)
            messagebox.showinfo('message', msg)
        
        else:
            msg = "Set search parameters to Customer_ID"
            messagebox.showinfo('message', msg)

        if(status):
            self.cuscustomerID.set("")
            self.cusname.set("")
            self.clickedTitle.set("")
            self.cusdob.set("XX.XX.XXXX")
            self.clickedGen.set("")
            self.cuscontactNo.set("0XXXXXXXXX")
            self.cusidNo.set("")
            self.cusemail.set("")
            self.cusnationality.set("")
            self.cusaddress.set("")
            self.clickedOption.set("")
            self.dataEntered.set("")
    
    def clearCusData(self):
        option = self.clickedOption.get()
        entered = self.dataEntered.get()
        msg,status = Customer.deleteCusfromDatabase(option,entered)
        messagebox.showinfo('message',msg)

        if(status):
            self.clickedOption.set("")
            self.dataEntered.set("")
            self.cuscustomerID.set("")
            self.cusname.set("")
            self.clickedTitle.set("")
            self.cusdob.set("XX.XX.XXXX")
            self.clickedGen.set("")
            self.cuscontactNo.set("0XXXXXXXXX")
            self.cusidNo.set("")
            self.cusemail.set("")
            self.cusnationality.set("")
            self.cusaddress.set("")
    
    def clearWindow(self):
        self.clickedOption.set("")
        self.dataEntered.set("")
        self.cuscustomerID.set("")
        self.cusname.set("")
        self.clickedTitle.set("")
        self.cusdob.set("XX.XX.XXXX")
        self.clickedGen.set("")
        self.cuscontactNo.set("0XXXXXXXXX")
        self.cusidNo.set("")
        self.cusemail.set("")
        self.cusnationality.set("")
        self.cusaddress.set("") """