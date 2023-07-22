import sqlite3
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Classes.CenterFunction import center
from Classes.Rooms import Rooms

class AdminRoomUpdate:
    def __init__(self,root):
        self.root = Toplevel(root)
        self.root.geometry("1000x600")
        self.root.update()
        self.root.title("Room Update Page")
        self.root.resizable(False, False)
        center(self.root,1000,600)

        imgLogin = PhotoImage(file="Images/Backgrounds/Gradient_background_3.png")
        Label(self.root, image=imgLogin).place(x=0, y=0,relwidth=1,relheight=1)

        #self.root.iconbitmap("Images/hnet.com-image.ico")  #For MacOS
        #self.root.iconphoto(False, PhotoImage(file = "Images/hnet.com-image.png")) #For Windows

        self.clickedCategory = StringVar()
        self.roomFloor = StringVar()
        self.roomNo = StringVar()
        self.clickedStatus = StringVar()
        self.clickedView = StringVar()
        self.roomPrice = IntVar()
        self.searchNo = StringVar()

        frame1 = Frame(self.root,bg="grey")
        frame1.place(x=80, y= 100, width=300, height=350)

        Label(self.root,text ="Manage Room Details",font=("times new roman",30,"bold")).place(x=490,y=50,anchor="center")

        Label(frame1,text ="Category").place(x=30,y=30)
        categoryOp = ["Single","Double","Triple","Quad","Queen","King","Twin","Suite"] # Dropdown menu options
        self.clickedCategory.set("") # initial menu text  
        OptionMenu(frame1,self.clickedCategory ,*categoryOp ).place(x=130,y=30)
        Label(frame1,text ="Floor").place(x=30,y=80)
        Entry(frame1,textvariable = self.roomFloor, font=('calibre',10,'normal')).place(x=130,y=80)
        Label(frame1,text ="RoomNo").place(x=30,y=130)
        Entry(frame1,textvariable = self.roomNo, font=('calibre',10,'normal')).place(x=130,y=130)
        Label(frame1,text ="Status").place(x=30,y=180)
        statusOp = ["Available","Booked","Repairing"] # Dropdown menu options
        self.clickedStatus.set("") # initial menu text  
        OptionMenu(frame1,self.clickedStatus ,*statusOp ).place(x=130,y=180)
        Label(frame1,text ="View").place(x=30,y=230)
        viewOp = ["City View","Ocean View"] # Dropdown menu options
        self.clickedView.set("") # initial menu text  
        OptionMenu(frame1,self.clickedView ,*viewOp ).place(x=130,y=230)
        Label(frame1,text ="Price").place(x=30,y=280)
        Entry(frame1,textvariable = self.roomPrice, font=('calibre',10,'normal')).place(x=130,y=280)

        frame2 = Frame(self.root,bg="grey")
        frame2.place(x=420, y= 100, width=530, height=400)

        Entry(frame2,textvariable = self.searchNo, font=('calibre',10,'normal')).place(x=100,y=50)
        Button(frame2,text="Search",relief=RAISED,command=self.showData).place(x=300,y=50)

        self.tree = ttk.Treeview(frame2, column=("c1", "c2", "c3", "c4","c5"), show='headings')

        self.tree.column("#1", anchor=tkinter.CENTER,width=60)
        self.tree.heading("#1", text="Room No.")
        self.tree.column("#2", anchor=tkinter.CENTER,width=80)
        self.tree.heading("#2", text="Category")
        self.tree.column("#3", anchor=tkinter.CENTER,width=100)
        self.tree.heading("#3", text="View")
        self.tree.column("#4", anchor=tkinter.CENTER,width=50)
        self.tree.heading("#4", text="Floor")
        self.tree.column("#5", anchor=tkinter.CENTER,width=80)
        self.tree.heading("#5", text="Status")
        self.tree.place(x=70,y=100)

        Button(frame2,text="Add",relief=RAISED,command=self.addRoomData).place(x=70,y=350)
        Button(frame2,text="Update",relief=RAISED,command=self.updateRoomData).place(x=170,y=350)
        Button(frame2,text="Delete",relief=RAISED,command=self.deleteRoomData).place(x=270,y=350)
        Button(frame2,text="Clear",relief=RAISED,command=self.clearWindow).place(x=370,y=350)

        self.root.mainloop()
    
    def showData(self):
        entered = self.searchNo.get()        
        data = Rooms.getData(entered)
        
        try:
            self.roomNo.set(data[0][0])
            self.clickedCategory.set(data[0][1])
            self.roomFloor.set(data[0][2])
            self.clickedStatus.set(data[0][3])
            self.clickedView.set(data[0][4])
            
            price = Rooms.getPrice(data[0][1])
            self.roomPrice.set(price)
        except IndexError as error:
            msg = "Data not matching. Try Again"
            messagebox.showinfo('message', msg)

        connection = sqlite3.connect("Databases/Hotel_Database.db")
        cursor1 = connection.cursor()
        data = "RoomNo,Category,View,Floor,Status"
        goal = "RoomNo"
        constrain = entered
        cursor1.execute("select %s from Room_Details where %s=?" % (data, goal), (constrain,))
        rows = cursor1.fetchall()    
        connection.close()

        for row in rows:
            self.tree.insert("", tkinter.END, values=row) 
            
    def addRoomData(self):
        roomNO = self.roomNo.get()
        category = self.clickedCategory.get()
        floor = self.roomFloor.get()
        status = self.clickedStatus.get()
        view = self.clickedView.get()
        
        status = Rooms.enterDatatoDatabase(roomNO,category,floor,status,view)
    
    def updateRoomData(self):
        entered = self.searchNo.get()
        status = True
        roomNO = self.roomNo.get()
        category = self.clickedCategory.get()
        floor = self.roomFloor.get()
        status = self.clickedStatus.get()
        view = self.clickedView.get()

        msg,status = Rooms.updateDatatoDatabase(roomNO,category,floor,status,view,entered)
        messagebox.showinfo('message', msg)

        if(status):
            self.roomNo.set("")
            self.clickedCategory.set("")
            self.roomFloor.set("")
            self.clickedStatus.set("")
            self.clickedView.set("")
            self.roomPrice.set("")
            self.searchNo.set("")
    
    def deleteRoomData(self):
        option = self.searchNo.get()
        msg,status = Rooms.deleteRoomfromDatabase(option)
        messagebox.showinfo('message',msg)

        if(status):
            self.roomNo.set("")
            self.clickedCategory.set("")
            self.roomFloor.set("")
            self.clickedStatus.set("")
            self.clickedView.set("")
            self.roomPrice.set("")
            self.searchNo.set("")

    def clearWindow(self):
        self.roomNo.set("")
        self.clickedCategory.set("")
        self.roomFloor.set("")
        self.clickedStatus.set("")
        self.clickedView.set("")
        self.roomPrice.set("")
        self.searchNo.set("")