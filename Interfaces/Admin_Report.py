import sqlite3
from tkinter import *
from tkinter import ttk
from Classes.CenterFunction import center

class AdminReport:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1000x600")
        self.root.update()
        self.root.title("Admin Booking Report")
        self.root.resizable(False, False)
        center(self.root,1000,600)

        self.name = None
        self.admUsername= StringVar()
        self.admPassword = StringVar()

        imgAdminLogin = PhotoImage(file="Images/Hotel_Admin_Login.png")
        Label(self.root,image=imgAdminLogin).place(x=0,y=0,relwidth=1,relheight=1)

        #self.root.iconbitmap("Images/hnet.com-image.ico")  #For MacOS
        #self.root.iconphoto(False, PhotoImage(file = "Images/hnet.com-image.png")) #For Windows

        data = self.fetch_data_from_database()

        frame = Frame(self.root, bg="grey")
        frame.place(x=0, y=0, width=1000, height=600)

        tree = ttk.Treeview(self.root)
        tree["columns"] = ("Booking ID", "CustomerID", "Name", "Check In", "Check Out", "No. of Adults", "No. of Child", "Meal Plan", "Room ID", "Total")

        # Define columns
        tree.column("#0", width=0, stretch=NO)
        for col in tree["columns"]:
            tree.column(col, anchor=CENTER)
            tree.heading(col, text=col, anchor=CENTER)

        # Insert data into the Treeview
        for row in data:
            tree.insert("", END, values=row)

        # Pack the Treeview into the root window
        tree.pack(expand=True, fill="both")

        self.root.mainloop()


    def fetch_data_from_database(self):
        connection = sqlite3.connect("Databases/Hotel_Database.db")
        cursor = connection.cursor()

        cursor.execute("SELECT Booking_ID, Customer_ID, Name, Check_IN, Check_OUT, No_of_Adults, No_of_Children, Meal_Plan, RoomNo, Total FROM Booking_Details")
        data = cursor.fetchall()
        connection.close()

        return data
