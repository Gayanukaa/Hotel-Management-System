from tkinter import *
from tkinter import messagebox
from Classes.CenterFunction import center
from Classes.Customer import Customer

class AdminCusUpdate:
    def __init__(self,root):
        self.root = Toplevel(root)
        self.root.geometry("1000x600")
        self.root.update()
        self.root.title("Customer Information Page")
        self.root.resizable(False, False)
        center(self.root,1000,600)

        img =  PhotoImage(file="Images/Backgrounds/Gradient_background_4.png")
        Label(self.root, image=img).place(x=0, y=0,relwidth=1,relheight=1)

        #self.root.iconbitmap("Images/hnet.com-image.ico")  #For MacOS
        #self.root.iconphoto(False, PhotoImage(file = "Images/hnet.com-image.png")) #For Windows

        self.cusname= StringVar()
        self.cusdob = StringVar()
        self.cuscontactNo = StringVar()
        self.cusidNo = IntVar()
        self.cusemail = StringVar()
        self.cusnationality = StringVar()
        self.cusaddress = StringVar()
        self.dataEntered = StringVar()
        self.cuscustomerID = StringVar()
        self.clickedOption = StringVar()
        self.clickedTitle = StringVar() # datatype of menu text
        self.clickedGen = StringVar()

        Label(self.root,text ="Customer Details",font=('calibre',20,'normal')).place(x=400,y=100)
        
        frame1 = Frame(self.root)
        frame1.place(x=270, y=40, width=450, height=50)

        options = ["Customer_ID","Name","Title","Date_of_Birth","Gender","Contact_No","ID_No","Email","Nationality","Address"] # Dropdown menu options
        self.clickedOption.set("Customer_ID") # initial menu text  
        OptionMenu(frame1,self.clickedOption ,*options ).place(x=30,y=10)
        Entry(frame1,textvariable = self.dataEntered, font=('calibre',10,'normal')).place(x=160, y=10)
        Button(frame1,text="Search",relief=RAISED,command=self.searchData).place(x=350,y=8)

        frame2 = Frame(self.root)
        frame2.place(x=90, y=150, width=780, height=320)

        Label(frame2,text ="Title").place(x=30,y=20)
        titleOp = ["Mr.","Ms.","Mrs."] # Dropdown menu options
        self.clickedTitle.set("") # initial menu text  
        cusTitle = OptionMenu(frame2,self.clickedTitle ,*titleOp ).place(x=80,y=20)
        Label(frame2,text ="Name").place(x=280,y=20)
        cusName = Entry(frame2,textvariable = self.cusname, font=('calibre',10,'normal')).place(x=350,y=20)
        Label(frame2,text ="Contact No.").place(x=530,y=20)
        cusContNo = Entry(frame2,textvariable = self.cuscontactNo, font=('calibre',10,'normal')).place(x=620, y=20)
        self.cuscontactNo.set("0XXXXXXXXX")
        
        Label(frame2,text ="D.O.B").place(x=30,y=120)
        cusDOB = Entry(frame2,textvariable = self.cusdob, font=('calibre',10,'normal')).place(x=80, y=120)
        self.cusdob.set("XX.XX.XXXX")
        Label(frame2,text ="Gender").place(x=280,y=120)
        genderOp = ["Male","Female","Prefer not to say"] # Dropdown menu options
        self.clickedGen.set("") # initial menu text  
        cusGender = OptionMenu(frame2,self.clickedGen ,*genderOp ).place(x=420,y=120) # Create Dropdown menu
        Label(frame2,text ="ID No.").place(x=530,y=120)
        cusId = Entry(frame2,textvariable = self.cusidNo, font=('calibre',10,'normal')).place(x=605, y=120)

        Label(frame2,text ="Email").place(x=30,y=220)
        cusEmail = Entry(frame2,textvariable = self.cusemail, font=('calibre',10,'normal')).place(x=80, y=220)
        Label(frame2,text ="Nationality").place(x=280,y=220)
        cusNat = Entry(frame2,textvariable = self.cusnationality, font=('calibre',10,'normal')).place(x=365, y=220)
        Label(frame2,text ="Address").place(x=530,y=220)
        cusAddrs = Entry(frame2,textvariable = self.cusaddress, font=('calibre',10,'normal')).place(x=605, y=220)

        frame3 = Frame(self.root)
        frame3.place(x=280, y=490, width=420, height=50)

        Button(frame3,text="Save",relief=RAISED,command=self.sendCusData).place(x=20,y=10)
        Button(frame3,text="Update",relief=RAISED,command=self.updateCusData).place(x=120,y=10)
        Button(frame3,text="Delete",relief=RAISED,command=self.deleteCusData).place(x=220,y=10)
        Button(frame3,text="Clear",relief=RAISED,command=self.clearWindow).place(x=320,y=10)

        self.root.mainloop()
    
    def searchData(self):
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
    
    def deleteCusData(self):
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
        self.cusaddress.set("")