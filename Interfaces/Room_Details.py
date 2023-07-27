""" import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from Classes.CenterFunction import center
from Classes.Rooms import Rooms

class RoomDetails:
    def __init__(self,root):
        self.root = Toplevel(root)
        self.root.geometry("1000x600")
        self.root.title("Room Details Page")
        self.root.resizable(False, False)
        center(self.root,1000,600)

        img = PhotoImage(file="Images/Backgrounds/Gradient_background_2.png")
        Label(self.root, image=img).pack()

        #self.root.iconbitmap("Images/hnet.com-image.ico")  #For MacOS
        #self.root.iconphoto(False, PhotoImage(file = "Images/hnet.com-image.png")) #For Windows


        # Create frames
        frame1 = ttk.Frame(self.root, width=1000, height=150)
        frame2 = ttk.Frame(self.root, width=1000, height=150)
        frame3 = ttk.Frame(self.root, width=1000, height=150)
        frame4 = ttk.Frame(self.root, width=1000, height=150)
        frame5 = ttk.Frame(self.root, width=1000, height=150)
        frame6 = ttk.Frame(self.root, width=1000, height=150)

        # Add frames to main window
        frame1.pack(side="top", fill="both", expand=True)
        frame2.pack(side="top", fill="both", expand=True)
        frame3.pack(side="top", fill="both", expand=True)
        frame4.pack(side="top", fill="both", expand=True)
        frame5.pack(side="top", fill="both", expand=True)
        frame6.pack(side="top", fill="both", expand=True)

        # Add text and image widgets to frames
        text1 = Text(frame1, height=10, width=50)
        text1.pack(side="left", fill="both", expand=True)
        text2 = Text(frame2, height=10, width=50)
        text2.pack(side="left", fill="both", expand=True)
        text3 = Text(frame3, height=10, width=50)
        text3.pack(side="left", fill="both", expand="both", expand=True)
        text4 = Text(frame4, height=10, width=50)
        text4.pack(side="left", fill="both", expand=True)
        text5 = Text(frame5, height=10, width=50)
        text5.pack(side="left", fill="both", expand=True)
        text6 = Text(frame6, height=10, width=50)
        text6.pack(side="left", fill="both", expand=True)
        
        # Add image to frame 1
        image1 = Image.open("image1.jpg")
        photo1 = ImageTk.PhotoImage(image1)
        label1 = tk.Label(frame1, image=photo1)
        label1.image = photo1
        label1.pack(side="right", fill="both", expand=True)
        # Add image to frame 2
        image2 = Image.open("image2.jpg")
        photo2 = ImageTk.PhotoImage(image2)
        label2 = tk.Label(frame2, image=photo2)
        label2.image = photo2
        label2.pack(side="right", fill="both", expand=True)
        # Add image to frame 3
        image3 = Image.open("image3.jpg")
        photo3 = ImageTk.PhotoImage(image3)
        label3 = tk.Label(frame3, image=photo3)
        label3.image = photo3
        label3.pack(side="right", fill="both", expand=True)
        # Add image to frame 4
        image4 = Image.open("image4.jpg")
        photo4 = ImageTk.PhotoImage(image4)
        label4 = tk.Label(frame4, image=photo4)
        label4.image = photo4
        label4.pack(side="right", fill="both", expand=True)
        # Add image to frame 5
        image5 = Image.open("image5.jpg")
        photo5 = ImageTk.PhotoImage(image5)
        label5 = tk.Label(frame5, image=photo5)


        

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