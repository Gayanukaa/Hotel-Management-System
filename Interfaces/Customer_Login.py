import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
from Classes.CenterFunction import center
from Customer_Interface import CustomerInterface
from Customer_Signup import CustomerSignUp

class CustomerLogin:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x800")
        self.root.update()
        self.root.title("Customer Login Window")
        self.root.resizable(False, False)
        center(self.root,1000,600)

        self.cusUsername= StringVar()
        self.cusPassword = StringVar()

        imgAdminLogin =  PhotoImage(file="Images/Hotel_Admin_Login.png")
        Label(self.root, image=imgAdminLogin).place(x=0, y=0,relwidth=1,relheight=1)
        #self.root.iconbitmap("Images/hnet.com-image.ico")  #For MacOS
        #self.root.iconphoto(False, PhotoImage(file = "Images/hnet.com-image.png")) #For Windows
        frame = Frame(self.root)
        frame.place(x=50, y=50, width=350, height=500)

        Label(frame,text ="Username", font=("times new roman",25, "bold")).pack(padx = 20, pady= 20)
        Entry(frame,textvariable = self.cusUsername, font=('calibre',15,'normal')).pack(padx = 20, pady= 20)
        Label(frame,text ="Password", font=("times new roman",25, "bold")).pack(padx = 20, pady= 20)
        Entry(frame,textvariable = self.cusPassword,show='*',font=('calibre',15,'normal')).pack(padx = 20, pady= 20)
        logBtn = Button(frame,text="Login",borderwidth=3,font=("times new roman",15,"bold"),command=self.logCustomerProcess)
        logBtn.pack(padx = 20, pady= 20)
        signBtn = Button(frame,text="Sign Up",borderwidth=3,font=("times new roman",15,"bold"),command=self.signupCustomerProcess) #command=self.openCusSignupWind
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

    def logCustomerProcess(self):
        username = self.cusUsername.get()
        password = self.cusPassword.get()

        msg = ""
        try:
            connection1 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorCus =connection1.cursor()
            data = "Username,Password"
            goal = "Username"
            constrain = username
            cursorCus.execute("select %s from Customer_Data where %s=?" % (data, goal), (constrain,))
            valideData = cursorCus.fetchall()
            connection1.close()
            data1 = valideData[0][0]
            data2 = valideData[0][1]

            if (data1 == username) and (data2 == password):
                msg = "Successful Login"
                status = True
            else:
                msg = "Incorrect Password"
                status = False
        except sqlite3.Error as error:
            msg = "Data entered not matching. Try Again"
            status = False
        except IndexError as error:
            msg = "Data entered not matching. Try Again"
            status = False
        finally:
            messagebox.showinfo('message', msg)
        if(status):
            CustomerInterface(self.root,username)
        else:
            pass

    def signupCustomerProcess(self):
        CustomerSignUp(self.root)


