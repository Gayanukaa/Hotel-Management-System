import tkinter as tk
from tkinter import ttk
from tkinter import *
from Classes.CenterFunction import center
from Classes.Rooms import Rooms

class RoomDetails:
    def __init__(self,root):
        self.root = Toplevel(root)
        self.root.geometry("1000x600")
        self.root.update()
        self.root.title("Room Details Page")
        self.root.resizable(False, False)
        center(self.root,1000,600)

        img = PhotoImage(file="Images/Backgrounds/Gradient_background_10.png")
        Label(self.root, image=img).pack()

        #self.root.iconbitmap("Images/hnet.com-image.ico")  #For MacOs
        #self.root.iconphoto(False, PhotoImage(file = "Images/hnet.com-image.png")) #For Windows
        
        Label(self.root, text="Room Details", font=("times new roman",30, "bold")).place(x=500,y=50, anchor="center") 
        
        buttonFrame = Frame(self.root)
        buttonFrame.place(x=40, y=100, width=140, height=470)
        
        Button(buttonFrame,text="Single Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=None).pack(padx = 10, pady= 17)
        Button(buttonFrame,text="Double Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=None).pack(padx = 10, pady= 17)
        Button(buttonFrame,text="Triple Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold")).pack(padx = 10, pady=17)
        Button(buttonFrame,text="Quad Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=None).pack(padx = 10, pady= 17)
        Button(buttonFrame,text="Queen Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold")).pack(padx = 10, pady= 17)
        Button(buttonFrame,text="King Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=None).pack(padx = 10, pady= 17)
        Button(buttonFrame,text="Twin Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold")).pack(padx = 10, pady= 17)

        self.singleFrame = Frame(self.root,width=770, height=500)
        self.singleFrame.place(x=210, y=80)
        
        singleRoom = PhotoImage(file="Images/Rooms/Single_Room_1.png",height=400,width=600)
        Label(self.singleFrame, image=singleRoom).place(x=0, y=0)
        
        #text description about single room
        Label(self.singleFrame, text="Single Room", font=("times new roman",20, "bold")).place(x=540,y=20)
        
        
        Label(self.singleFrame, text="Room Size: 20m2", font=("times new roman",15, "bold")).place(x=430,y=80)
        Label(self.singleFrame, text="Bed Size: 1 Single Bed", font=("times new roman",15, "bold")).place(x=430,y=120)
        Label(self.singleFrame, text="Max People: 1", font=("times new roman",15, "bold")).place(x=430,y=160)
        Label(self.singleFrame, text="Room View: City View", font=("times new roman",15, "bold")).place(x=430,y=200)
        Label(self.singleFrame, text="Room Price: $100", font=("times new roman",15, "bold")).place(x=430,y=240)
        Label(self.singleFrame, text="Room Description: ", font=("times new roman",15, "bold")).place(x=430,y=280)
        Label(self.singleFrame, text="This room is a single room with a single bed.\nIt has a city view and is 20m2 in size.", font=("times new roman",15, "bold")).place(x=440,y=320)
        
        Button(self.singleFrame,text="Book Now",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.destroy).place(x=350,y=450)
        
        
        self.root.mainloop()
        
    def destroy(self):
        self.singleFrame.destroy()
        
    """
        self.currentPage = 1
        self.showPage(0)

        leftBtn = Button(self.root,text="<",borderwidth=3,font=("times new roman",15,"bold"),command=self.showPage(-1))
        leftBtn.place(x = 420, y= 550)

        rightBtn = Button(self.root,text=">",borderwidth=3,font=("times new roman",15,"bold"),command=self.showPage(1))
        rightBtn.place(x = 520, y= 550)

        self.root.mainloop()
    
    def showPage(self, n):
        self.currentPage += n

        if(self.currentPage == 1):
            frame1 = Frame(self.root,bg="grey",width=1000,height=500)
            frame1.pack()

            singleRoom = PhotoImage(file="Images/Rooms/Single_Room_1.png",height=200,width=200)
            Label(frame1, image=singleRoom).place(x=0,y=50)
            
            doubleRoom = PhotoImage(file="Images/Rooms/Double_Room_1.png")
            Label(frame1, image=doubleRoom).place(x=500,y=50)
        
        elif(self.currentPage == 2):
            frame2 = Frame(self.root,bg="grey",width=1000,height=500)
            frame2.pack()

            tripleRoom = PhotoImage(file="Images/Rooms/Triple_Room_1.png",height=200,width=200)
            Label(frame2, image=tripleRoom).place(x=0,y=50)
            
            quadRoom = PhotoImage(file="Images/Rooms/Quad_Room_1.png")
            Label(frame2, image=quadRoom).place(x=500,y=50)
        
        elif(self.currentPage == 3):
            frame3 = Frame(self.root,bg="grey",width=1000,height=500)
            frame3.pack()

            queenRoom = PhotoImage(file="Images/Rooms/Queen_Room_1.png",height=200,width=200)
            Label(frame3, image=queenRoom).place(x=0,y=50)
            
            kingRoom = PhotoImage(file="Images/Rooms/King_Room_1.png")
            Label(frame3, image=kingRoom).place(x=500,y=50)
        
        elif(self.currentPage == 4):
            frame4 = Frame(self.root,bg="grey",width=1000,height=500)
            frame4.pack()

            suiteRoom = PhotoImage(file="Images/Rooms/Suite_Room_1.png",height=200,width=200)
            Label(frame4, image=suiteRoom).place(x=0,y=50)
            
            twinRoom = PhotoImage(file="Images/Rooms/Twin_Room_1.png")
            Label(frame4, image=twinRoom).place(x=500,y=50)

        else:
            print("Error")
    """