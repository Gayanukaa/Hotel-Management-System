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
        
        Button(buttonFrame,text="Single Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.showSingle).pack(padx = 10, pady= 17)
        Button(buttonFrame,text="Double Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.showDouble).pack(padx = 10, pady= 17)
        Button(buttonFrame,text="Triple Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold")).pack(padx = 10, pady=17)
        Button(buttonFrame,text="Quad Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=None).pack(padx = 10, pady= 17)
        Button(buttonFrame,text="Queen Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold")).pack(padx = 10, pady= 17)
        Button(buttonFrame,text="King Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=None).pack(padx = 10, pady= 17)
        Button(buttonFrame,text="Twin Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold")).pack(padx = 10, pady= 17)

        self.singleFrame = Frame(self.root,width=770, height=500)
        self.singleFrame.place(x=210, y=80)
        
        self.singleRoom = PhotoImage(file="Images/Rooms/Single_Room_1.png",height=400,width=600)
        Label(self.singleFrame, image=self.singleRoom).place(x=0, y=0)
        
        #text description about single room
        Label(self.singleFrame, text="Single Room", font=("times new roman",20, "bold")).place(x=540,y=20)
        
        self.dimensionFrame = Frame(self.singleFrame,width=150,height=55)
        self.dimensionFrame.place(x=420,y=80)
        self.dimension = PhotoImage(file="Images/Icons/dimensions_icon.png")
        Label(self.dimensionFrame, image=self.dimension).place(x=0, y=0)        
        Label(self.dimensionFrame, text="Room Size: 37 m2 to 45 m2", font=("times new roman",15, "bold"),fg="black").place(x=55,y=2)
        
        #wifiFrame
        self.wifiFrame = Frame(self.singleFrame,width=150,height=55)
        self.wifiFrame.place(x=610,y=80)  
        self.wifi = PhotoImage(file="Images/Icons/hotel_wifi_icon.png")
        Label(self.wifiFrame, image=self.wifi).place(x=0, y=0)   
        Label(self.wifiFrame, text="Wifi: Yes", font=("times new roman",15, "bold"),fg="black").place(x=55,y=2)
                
        Label(self.singleFrame, text="Bed Size: 1 Single Bed", font=("times new roman",15, "bold")).place(x=420,y=160)
        Label(self.singleFrame, text="Max People: 1", font=("times new roman",15, "bold")).place(x=420,y=200)
        Label(self.singleFrame, text="Room View: City View or Ocean View", font=("times new roman",15, "bold")).place(x=420,y=240)
        Label(self.singleFrame, text="Room Price: Rs.10,000", font=("times new roman",15, "bold")).place(x=420,y=280)
        Label(self.singleFrame, text="Room Description: ", font=("times new roman",15, "bold")).place(x=420,y=330)
        Label(self.singleFrame, text="This room is a single room with a single bed.", font=("times new roman",15, "bold")).place(x=440,y=355)
        Label(self.singleFrame, text="It has a city view and is 37m2 in size.", font=("times new roman",15, "bold")).place(x=440,y=375)
        
        Button(self.singleFrame,text="Book Now",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.destroySingle).place(x=350,y=450)
        
        self.root.mainloop()
        
    def showSingle(self):
        self.singleFrame = Frame(self.root,width=770, height=500)
        self.singleFrame.place(x=210, y=80)
        
        self.singleRoom = PhotoImage(file="Images/Rooms/Single_Room_1.png",height=400,width=600)
        Label(self.singleFrame, image=self.singleRoom).place(x=0, y=0)
        
        #text description about single room
        Label(self.singleFrame, text="Single Room", font=("times new roman",20, "bold")).place(x=540,y=20)
        
        self.dimensionFrame = Frame(self.singleFrame,width=150,height=55)
        self.dimensionFrame.place(x=420,y=80)
        self.dimension = PhotoImage(file="Images/Icons/dimensions_icon.png")
        Label(self.dimensionFrame, image=self.dimension).place(x=0, y=0)        
        Label(self.dimensionFrame, text="Room Size: 37 m2 to 45 m2", font=("times new roman",15, "bold"),fg="black").place(x=55,y=2)
        
        #wifiFrame
        self.wifiFrame = Frame(self.singleFrame,width=150,height=55)
        self.wifiFrame.place(x=610,y=80)  
        self.wifi = PhotoImage(file="Images/Icons/hotel_wifi_icon.png")
        Label(self.wifiFrame, image=self.wifi).place(x=0, y=0)   
        Label(self.wifiFrame, text="Wifi: Yes", font=("times new roman",15, "bold"),fg="black").place(x=55,y=2)
                
        Label(self.singleFrame, text="Bed Size: 1 Single Bed", font=("times new roman",15, "bold")).place(x=420,y=160)
        Label(self.singleFrame, text="Max People: 1", font=("times new roman",15, "bold")).place(x=420,y=200)
        Label(self.singleFrame, text="Room View: City View or Ocean View", font=("times new roman",15, "bold")).place(x=420,y=240)
        Label(self.singleFrame, text="Room Price: Rs.10,000", font=("times new roman",15, "bold")).place(x=420,y=280)
        Label(self.singleFrame, text="Room Description: ", font=("times new roman",15, "bold")).place(x=420,y=330)
        Label(self.singleFrame, text="This room is a single room with a single bed.", font=("times new roman",15, "bold")).place(x=440,y=355)
        Label(self.singleFrame, text="It has a city view and is 37m2 in size.", font=("times new roman",15, "bold")).place(x=440,y=375)
        
        Button(self.singleFrame,text="Book Now",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.destroySingle).place(x=350,y=450)
        
    def showDouble(self):
        self.singleFrame = Frame(self.root,width=770, height=500)
        self.singleFrame.place(x=210, y=80)
        
        self.singleRoom = PhotoImage(file="Images/Rooms/Double_Room_1.png",height=400,width=600)
        Label(self.singleFrame, image=self.singleRoom).place(x=0, y=0)
        
        #text description about single room
        Label(self.singleFrame, text="Double Room", font=("times new roman",20, "bold")).place(x=540,y=20)
        
        self.dimensionFrame = Frame(self.singleFrame,width=150,height=55)
        self.dimensionFrame.place(x=420,y=80)
        self.dimension = PhotoImage(file="Images/Icons/dimensions_icon.png")
        Label(self.dimensionFrame, image=self.dimension).place(x=0, y=0)        
        Label(self.dimensionFrame, text="Room Size: 40 m2 to 45 m2", font=("times new roman",15, "bold"),fg="black").place(x=55,y=2)
        
        #wifiFrame
        self.wifiFrame = Frame(self.singleFrame,width=150,height=55)
        self.wifiFrame.place(x=610,y=80)  
        self.wifi = PhotoImage(file="Images/Icons/hotel_wifi_icon.png")
        Label(self.wifiFrame, image=self.wifi).place(x=0, y=0)   
        Label(self.wifiFrame, text="Wifi: Yes", font=("times new roman",15, "bold"),fg="black").place(x=55,y=2)
                
        Label(self.singleFrame, text="Bed Size: 1 Double Bed or 2 Single Beds", font=("times new roman",15, "bold")).place(x=420,y=160)
        Label(self.singleFrame, text="Max People: 2", font=("times new roman",15, "bold")).place(x=420,y=200)
        Label(self.singleFrame, text="Room View: City View or Ocean View", font=("times new roman",15, "bold")).place(x=420,y=240)
        Label(self.singleFrame, text="Room Price: Rs.15,000", font=("times new roman",15, "bold")).place(x=420,y=280)
        Label(self.singleFrame, text="Room Description: ", font=("times new roman",15, "bold")).place(x=420,y=330)
        Label(self.singleFrame, text="This room is a single room with a single bed.", font=("times new roman",15, "bold")).place(x=440,y=355)
        Label(self.singleFrame, text="It has a city view and is 40m2 in size.", font=("times new roman",15, "bold")).place(x=440,y=375)
        
        Button(self.singleFrame,text="Book Now",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.destroySingle).place(x=350,y=450)
          
    def destroySingle(self):
        self.singleFrame.destroy()
        
        self.stillFrame = Frame(self.root,width=770, height=500, bg="grey")
        self.stillFrame.place(x=210, y=80)
        
        Label(self.stillFrame, text="Choose a Room", font=("times new roman",20, "bold")).place(x=340,y=240)
        
