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
        Button(buttonFrame,text="Triple Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.showTriple).pack(padx = 10, pady=17)
        Button(buttonFrame,text="Quad Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.showQuad).pack(padx = 10, pady= 17)
        Button(buttonFrame,text="Queen Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold")).pack(padx = 10, pady= 17)
        Button(buttonFrame,text="King Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=None).pack(padx = 10, pady= 17)
        Button(buttonFrame,text="Twin Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold")).pack(padx = 10, pady= 17)

        self.roomFrame = Frame(self.root,width=770, height=500)
        self.roomFrame.place(x=210, y=80)
        
        self.roomImage = PhotoImage(file="Images/Rooms/Single_Room_1.png",height=400,width=600)
        Label(self.roomFrame, image=self.roomImage).place(x=0, y=0)
        
        self.showSingle()
        
        self.root.mainloop()
        
    def showSingle(self):
        self.roomFrame = Frame(self.root,width=770, height=500)
        self.roomFrame.place(x=210, y=80)
        
        self.roomImage = PhotoImage(file="Images/Rooms/Single_Room_1.png",height=400,width=600)
        Label(self.roomFrame, image=self.roomImage).place(x=0, y=0)
        
        #text description about single room
        Label(self.roomFrame, text="Single Room", font=("times new roman",20, "bold")).place(x=540,y=20)
        
        self.dimensionFrame = Frame(self.roomFrame,width=150,height=55)
        self.dimensionFrame.place(x=420,y=80)
        self.dimension = PhotoImage(file="Images/Icons/dimensions_icon.png")
        Label(self.dimensionFrame, image=self.dimension).place(x=0, y=0)        
        Label(self.dimensionFrame, text="Room Size:\n37m2 to 45m2", font=("times new roman",15, "bold"),fg="black").place(x=55,y=2)
        
        #wifiFrame
        self.wifiFrame = Frame(self.roomFrame,width=160,height=55)
        self.wifiFrame.place(x=610,y=80)  
        self.wifi = PhotoImage(file="Images/Icons/hotel_wifi_icon.png")
        Label(self.wifiFrame, image=self.wifi).place(x=0, y=0)   
        Label(self.wifiFrame, text="Wifi: Yes", font=("times new roman",15, "bold"),fg="black").place(x=55,y=2)
                
        Label(self.roomFrame, text="Bed Size: 1 Single Bed", font=("times new roman",15, "bold")).place(x=420,y=160)
        Label(self.roomFrame, text="Max People: 1", font=("times new roman",15, "bold")).place(x=420,y=200)
        Label(self.roomFrame, text="Room View: City View or Ocean View", font=("times new roman",15, "bold")).place(x=420,y=240)
        Label(self.roomFrame, text="Room Price: Rs.10,000", font=("times new roman",15, "bold")).place(x=420,y=280)
        Label(self.roomFrame, text="Room Description: ", font=("times new roman",15, "bold")).place(x=420,y=330)
        Label(self.roomFrame, text="This room is a single room with a single bed.", font=("times new roman",15, "bold")).place(x=440,y=355)
        Label(self.roomFrame, text="It has a nice view and is 37m2 in size.", font=("times new roman",15, "bold")).place(x=440,y=375)
        
        Button(self.roomFrame,text="Book Now",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.destroySingle).place(x=350,y=450)
        
    def showDouble(self):
        self.roomFrame = Frame(self.root,width=770, height=500)
        self.roomFrame.place(x=210, y=80)
        
        self.roomImage = PhotoImage(file="Images/Rooms/Double_Room_1.png",height=400,width=600)
        Label(self.roomFrame, image=self.roomImage).place(x=0, y=0)
        
        #text description about single room
        Label(self.roomFrame, text="Double Room", font=("times new roman",20, "bold")).place(x=540,y=20)
        
        self.dimensionFrame = Frame(self.roomFrame,width=160,height=55)
        self.dimensionFrame.place(x=420,y=80)
        self.dimension = PhotoImage(file="Images/Icons/dimensions_icon.png")
        Label(self.dimensionFrame, image=self.dimension).place(x=0, y=0)        
        Label(self.dimensionFrame, text="Room Size:\n40m2 to 45m2", font=("times new roman",15, "bold"),fg="black").place(x=55,y=2)
        
        #wifiFrame
        self.wifiFrame = Frame(self.roomFrame,width=150,height=55)
        self.wifiFrame.place(x=610,y=80)  
        self.wifi = PhotoImage(file="Images/Icons/hotel_wifi_icon.png")
        Label(self.wifiFrame, image=self.wifi).place(x=0, y=0)   
        Label(self.wifiFrame, text="Wifi: Yes", font=("times new roman",15, "bold"),fg="black").place(x=55,y=2)
                
        Label(self.roomFrame, text="Bed Size: 1 Double Bed or 2 Single Beds", font=("times new roman",15, "bold")).place(x=420,y=160)
        Label(self.roomFrame, text="Max People: 2", font=("times new roman",15, "bold")).place(x=420,y=200)
        Label(self.roomFrame, text="Room View: City View or Ocean View", font=("times new roman",15, "bold")).place(x=420,y=240)
        Label(self.roomFrame, text="Room Price: Rs.15,000", font=("times new roman",15, "bold")).place(x=420,y=280)
        Label(self.roomFrame, text="Room Description: ", font=("times new roman",15, "bold")).place(x=420,y=330)
        Label(self.roomFrame, text="This room is a double room with two bed options.", font=("times new roman",15, "bold")).place(x=440,y=355)
        Label(self.roomFrame, text="It has a great view and is 40m2 in size.", font=("times new roman",15, "bold")).place(x=440,y=375)
        
        Button(self.roomFrame,text="Book Now",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.destroySingle).place(x=350,y=450)
        
    def showTriple(self):
        self.roomFrame = Frame(self.root,width=770, height=500)
        self.roomFrame.place(x=210, y=80)
        
        self.roomImage = PhotoImage(file="Images/Rooms/Triple_Room_1.png",height=400,width=600)
        Label(self.roomFrame, image=self.roomImage).place(x=0, y=0)
        
        #text description about single room
        Label(self.roomFrame, text="Triple Room", font=("times new roman",20, "bold")).place(x=540,y=20)
        
        self.dimensionFrame = Frame(self.roomFrame,width=160,height=55)
        self.dimensionFrame.place(x=420,y=80)
        self.dimension = PhotoImage(file="Images/Icons/dimensions_icon.png")
        Label(self.dimensionFrame, image=self.dimension).place(x=0, y=0)        
        Label(self.dimensionFrame, text="Room Size:\n45m2 to 65m2", font=("times new roman",15, "bold"),fg="black").place(x=55,y=2)
        
        #wifiFrame
        self.wifiFrame = Frame(self.roomFrame,width=150,height=55)
        self.wifiFrame.place(x=610,y=80)  
        self.wifi = PhotoImage(file="Images/Icons/hotel_wifi_icon.png")
        Label(self.wifiFrame, image=self.wifi).place(x=0, y=0)   
        Label(self.wifiFrame, text="Wifi: Yes", font=("times new roman",15, "bold"),fg="black").place(x=55,y=2)
                
        Label(self.roomFrame, text="Bed Size: 3 Twin Beds or 1 Double 1 and Twin Bed", font=("times new roman",15, "bold")).place(x=420,y=160)
        Label(self.roomFrame, text="Max People: 3", font=("times new roman",15, "bold")).place(x=420,y=200)
        Label(self.roomFrame, text="Room View: City View or Ocean View", font=("times new roman",15, "bold")).place(x=420,y=240)
        Label(self.roomFrame, text="Room Price: Rs.20,000", font=("times new roman",15, "bold")).place(x=420,y=280)
        Label(self.roomFrame, text="Room Description: ", font=("times new roman",15, "bold")).place(x=420,y=330)
        Label(self.roomFrame, text="This room is a triple room with a single beds.", font=("times new roman",15, "bold")).place(x=440,y=355)
        Label(self.roomFrame, text="It has an amazing view and is 45m2 in size.", font=("times new roman",15, "bold")).place(x=440,y=375)
        
        Button(self.roomFrame,text="Book Now",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.destroySingle).place(x=350,y=450)
        
    def showQuad(self):
        self.roomFrame = Frame(self.root,width=770, height=500)
        self.roomFrame.place(x=210, y=80)
        
        self.roomImage = PhotoImage(file="Images/Rooms/Quad_Room_1.png",height=400,width=600)
        Label(self.roomFrame, image=self.roomImage).place(x=0, y=0)
        
        #text description about single room
        Label(self.roomFrame, text="Quad Room", font=("times new roman",20, "bold")).place(x=540,y=20)
        
        self.dimensionFrame = Frame(self.roomFrame,width=160,height=55)
        self.dimensionFrame.place(x=420,y=80)
        self.dimension = PhotoImage(file="Images/Icons/dimensions_icon.png")
        Label(self.dimensionFrame, image=self.dimension).place(x=0, y=0)        
        Label(self.dimensionFrame, text="Room Size:\n70m2 to 85m2", font=("times new roman",15, "bold"),fg="black").place(x=55,y=2)
        
        #wifiFrame
        self.wifiFrame = Frame(self.roomFrame,width=150,height=55)
        self.wifiFrame.place(x=610,y=80)  
        self.wifi = PhotoImage(file="Images/Icons/hotel_wifi_icon.png")
        Label(self.wifiFrame, image=self.wifi).place(x=0, y=0)   
        Label(self.wifiFrame, text="Wifi: Yes", font=("times new roman",15, "bold"),fg="black").place(x=55,y=2)
                
        Label(self.roomFrame, text="Bed Size: 2 Double Beds", font=("times new roman",15, "bold")).place(x=420,y=160)
        Label(self.roomFrame, text="Max People: 4", font=("times new roman",15, "bold")).place(x=420,y=200)
        Label(self.roomFrame, text="Room View: City View or Ocean View", font=("times new roman",15, "bold")).place(x=420,y=240)
        Label(self.roomFrame, text="Room Price: Rs.25,000", font=("times new roman",15, "bold")).place(x=420,y=280)
        Label(self.roomFrame, text="Room Description: ", font=("times new roman",15, "bold")).place(x=420,y=330)
        Label(self.roomFrame, text="This room is a quad room with double beds.", font=("times new roman",15, "bold")).place(x=440,y=355)
        Label(self.roomFrame, text="It has an amazing view and is 70m2 in size.", font=("times new roman",15, "bold")).place(x=440,y=375)
        
        Button(self.roomFrame,text="Book Now",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.destroySingle).place(x=350,y=450)
        
        
                                                                                                                                                                    
          
    def destroySingle(self):
        self.roomFrame.destroy()
        
        self.stillFrame = Frame(self.root,width=770, height=500, bg="grey")
        self.stillFrame.place(x=210, y=80)
        
        Label(self.stillFrame, text="Choose a Room", font=("times new roman",20, "bold")).place(x=340,y=240)
        
