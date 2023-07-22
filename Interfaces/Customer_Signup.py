from tkinter import *
from tkinter import messagebox 
from Classes.CenterFunction import center
from Classes.Customer import Customer

class CustomerSignUp:
    def __init__(self,root):
        self.root = Toplevel(root)
        self.root.geometry("1000x600")
        self.root.update()
        self.root.title("Customer SignUp Page")
        self.root.resizable(False, False)
        center(self.root,1000,600)

        imgSignUp =  PhotoImage(file="Images/Backgrounds/Gradient_background_3.png")
        Label(self.root, image=imgSignUp).place(x=0, y=0,relwidth=1,relheight=1)

        #self.root.iconbitmap("Images/hnet.com-image.ico")  #For MacOS
        #self.root.iconphoto(False, PhotoImage(file = "Images/hnet.com-image.png")) #For Windows        

        self.cusname= StringVar()
        self.cuspassw= StringVar()
        self.cusdob = StringVar()
        self.cuscontactNo = StringVar()
        self.cusidNo = StringVar()
        self.cusemail = StringVar()
        self.cusnationality = StringVar()
        self.cusaddress = StringVar()
        self.cususername = StringVar()
        self.cusConpass = StringVar()

        Label(self.root,text ="Customer Details",font=('calibre',25,'normal')).place(x=410,y=45)

        frame1 = Frame(self.root,bg="grey")
        frame1.place(x=80, y=100, width=835, height=360)

        Label(frame1,text ="Title").place(x=20,y=20)
        titleOp = ["Mr.","Ms.","Mrs."] # Dropdown menu options
        self.clickedTitle = StringVar() # datatype of menu text
        self.clickedTitle.set("") # initial menu text  
        cusTitle = OptionMenu(frame1,self.clickedTitle ,*titleOp ).place(x=120,y=20)
        Label(frame1,text ="Name").place(x=300,y=20)
        cusName = Entry(frame1,textvariable = self.cusname, font=('calibre',10,'normal')).place(x=400,y=20)
        Label(frame1,text ="Contact No.").place(x=570,y=20)
        cusContNo = Entry(frame1,textvariable = self.cuscontactNo, font=('calibre',10,'normal')).place(x=670, y=20)
        self.cuscontactNo.set("0XXXXXXXXX")

        Label(frame1,text ="D.O.B").place(x=20,y=120)
        cusDOB = Entry(frame1,textvariable = self.cusdob, font=('calibre',10,'normal')).place(x=120, y=120)
        self.cusdob.set("XX.XX.XXXX")
        Label(frame1,text ="Gender").place(x=300,y=120)
        genderOp = ["Male","Female","Prefer not to say"] # Dropdown menu options
        self.clickedGen = StringVar() # datatype of menu text
        self.clickedGen.set("") # initial menu text  
        cusGender = OptionMenu(frame1,self.clickedGen ,*genderOp ).place(x=400,y=120) # Create Dropdown menu
        Label(frame1,text ="ID No.").place(x=570,y=120)
        cusId = Entry(frame1,textvariable = self.cusidNo, font=('calibre',10,'normal')).place(x=670, y=120)

        Label(frame1,text ="Email").place(x=20,y=220)
        cusEmail = Entry(frame1,textvariable = self.cusemail, font=('calibre',10,'normal')).place(x=120, y=220)
        Label(frame1,text ="Nationality").place(x=300,y=220)
        cusNat = Entry(frame1,textvariable = self.cusnationality, font=('calibre',10,'normal')).place(x=400, y=220)
        Label(frame1,text ="Address").place(x=570,y=220)
        cusAddrs = Entry(frame1,textvariable = self.cusaddress, font=('calibre',10,'normal')).place(x=670, y=220)

        Label(frame1,text ="Username").place(x=20,y=320)
        cusUsername = Entry(frame1,textvariable = self.cususername, font=('calibre',10,'normal')).place(x=120, y=320)
        Label(frame1,text ="Password").place(x=300,y=320)
        cusPassword = Entry(frame1,textvariable = self.cuspassw, font=('calibre',10,'normal'),show='*').place(x=400, y=320)
        Label(frame1,text ="Confirm PW").place(x=570,y=320)
        cusConPass = Entry(frame1,textvariable = self.cusConpass, font=('calibre',10,'normal'),show='*').place(x=670, y=320)

        frame2 = Frame(self.root,bg="grey")
        frame2.place(x=340, y=490, width=335, height=50)

        Button(frame2,text="Check Password",relief=RAISED,command=self.validation).place(x=20,y=10)
        Button(frame2,text="Create Account",relief=RAISED,command=self.sendCusData).place(x=180,y=10)

        self.root.mainloop()
    
    def validation(self):
            special_ch = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']
            password = self.cuspassw.get()
            conPassword = self.cusConpass.get()
            msg = ""
                
            if len(password) == 0: msg = 'Password can\'t be empty \n'
            elif not(password == conPassword): msg = 'Passwords do not match \n'
            else:
                try:
                    if not any(ch in special_ch for ch in password):
                        msg = 'Atleast 1 special character required! \n'
                    if not any(ch.isupper() for ch in password):
                        msg = 'Atleast 1 uppercase character required! \n'
                    if not any(ch.islower() for ch in password):
                        msg = 'Atleast 1 lowercase character required! \n'
                    if not any(ch.isdigit() for ch in password):
                        msg = 'Atleast 1 number required! \n'
                    if len(password) < 8:
                        msg = 'Password must be minimum of 8 characters! \n'
                    else:
                        msg = 'Password Accepted!' 
                except Exception as ep:
                    messagebox.showerror('error', ep)
            messagebox.showinfo('message', msg)   
            
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
        customer.username = self.cususername.get()
        customer.password = self.cuspassw.get()
        
        status = customer.enterDatatoDatabase(customer.name,customer.title,customer.dob,customer.gender,customer.contactNo,customer.idNo,customer.email,customer.nationality,customer.address,customer.username,customer.password)
        if(status):
            self.cusname.set("")
            self.clickedTitle.set("")
            self.cusdob.set("XX.XX.XXXX")
            self.clickedGen.set("")
            self.cuscontactNo.set("0XXXXXXXXX")
            self.cusidNo.set("")
            self.cusemail.set("")
            self.cusnationality.set("")
            self.cusaddress.set("")
            self.cususername.set("")
            self.cuspassw.set("")
            self.cusConpass.set("")
            self.root.destroy()
            self.root.update()
        else: pass