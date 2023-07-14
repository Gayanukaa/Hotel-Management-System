import sqlite3
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Classes.CenterFunction import center
from Admin_Interface import AdminInterface
from Classes.Admin import Admin
#admin - admin

class AdminLogin:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1000x600")
        self.root.update()
        self.root.title("Admin Login Page")
        self.root.resizable(False, False)
        center(self.root,1000,600)

        self.name = None
        self.admUsername= StringVar()
        self.admPassword = StringVar()

        imgAdminLogin = PhotoImage(file="Images/Hotel_Admin_Login.png")
        Label(self.root,image=imgAdminLogin).place(x=0,y=0,relwidth=1,relheight=1)

        #self.root.iconbitmap("Images/hnet.com-image.ico")  #For MacOS
        #self.root.iconphoto(False, PhotoImage(file = "Images/hnet.com-image.png")) #For Windows

        frame = Frame(self.root)
        frame.place(x=50, y=50, width=350, height=500)

        Label(frame,text ="Username", font=("times new roman",25, "bold")).pack(padx = 20, pady= 20)
        Entry(frame,textvariable = self.admUsername, font=('calibre',15,'normal')).pack(padx = 20, pady= 20)
        Label(frame,text ="Password", font=("times new roman",25, "bold")).pack(padx = 20, pady= 20)
        Entry(frame,textvariable = self.admPassword,show='*',font=('calibre',15,'normal')).pack(padx = 20, pady= 20)
        logBtn = Button(frame,text="Login",borderwidth=3,font=("times new roman",15,"bold"),command=self.logAdminProcess)
        logBtn.pack(padx = 20, pady= 20)
        signBtn = Button(frame,text="Sign Up",borderwidth=3,font=("times new roman",15,"bold"),command=self.signupAdminProcess)
        signBtn.pack(padx = 20, pady= 20)

        # =======Display Rooms=========

        self.tree = ttk.Treeview(self.root, column=("c1", "c2", "c3", "c4"), show='headings')
        self.tree.column("#1", anchor=tkinter.CENTER,width=150)
        self.tree.heading("#1", text="Category")
        self.tree.column("#2", anchor=tkinter.CENTER,width=150)
        self.tree.heading("#2", text="View")
        self.tree.column("#3", anchor=tkinter.CENTER,width=80)
        self.tree.heading("#3", text="Floor")
        self.tree.column("#4", anchor=tkinter.CENTER,width=150)
        self.tree.heading("#4", text="Status")
        self.tree.place(x=450,y=200)
        Button(self.root,text="Display Room Status",command=self.View).place(x=630,y=150)

        self.root.mainloop()
 
    def View(self):
        connection = sqlite3.connect("Databases/Hotel_Database.db")
        cursor = connection.cursor()
        cursor.execute("SELECT Category,View,Floor,Status FROM Room_Details order by Floor")
        rows = cursor.fetchall()    

        for row in rows:
            self.tree.insert("", tkinter.END, values=row)        

        connection.close()

    def logAdminProcess(self):
        username = self.admUsername.get()
        password = self.admPassword.get()
        
        msg,status = Admin.validateLogin(username,password)
        
        messagebox.showinfo('message', msg)
        if(status):
            AdminInterface(self.root,username)
        else:
            pass

    def signupAdminProcess(self):
        msg = "For new Admins contact HR for details"
        messagebox.showinfo('message', msg)     #implement a website url contact HR