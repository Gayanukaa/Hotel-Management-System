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

        img = PhotoImage(file="Images/Backgrounds/Gradient_background_9.png")
        Label(self.root, image=img).pack()

        #self.root.iconbitmap("Images/hnet.com-image.ico")  #For MacOs
        #self.root.iconphoto(False, PhotoImage(file = "Images/hnet.com-image.png")) #For Windows
        
        
       
        self.root.mainloop()
        
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