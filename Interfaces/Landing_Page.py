from tkinter import *
from Customer_Login import CustomerLogin
from Admin_Login import AdminLogin
from Classes.CenterFunction import center

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)
        center(self.root,1000,600)

        # ======Background image==========
        imgLogin =  PhotoImage(file="Images/Hotel_Login.png")
        Label(self.root, image=imgLogin).place(x=0, y=0,relwidth=1,relheight=1)

        #self.root.iconbitmap("Images/hnet.com-image.ico")  #For MacOS
        #self.root.iconphoto(False, PhotoImage(file = "Images/hnet.com-image.png")) #For Windows
        
        Label(self.root, text="Choose your Login", font=("times new roman",30, "bold")).place(x=500,y=100, anchor="center")

        frame1 = Frame(self.root,bg="white")
        frame1.place(x=105, y=420, width=158, height=40)
        admBtn = Button(frame1,text="Admin Login",borderwidth=5,font=("times new roman",20,"bold"),bg="red",fg="grey",command=self.adminLogin)
        admBtn.pack()

        frame2 = Frame(self.root,bg="white")
        frame2.place(x=695, y=420, width=185, height=40)
        cusBtn = Button(frame2,text="Customer Login",borderwidth=5,font=("times new roman",20,"bold"),bg="red",fg="grey",command=self.customerLogin)
        cusBtn.pack()
        
        self.root.mainloop()
    
    def adminLogin(self):
        #self.root.destroy()
        #root = Tk()
        AdminLogin(self.root)
    
    def customerLogin(self):
        #self.root.destroy()
        #root = Tk()
        CustomerLogin(self.root)

root = Tk()
obj = Login(root)
