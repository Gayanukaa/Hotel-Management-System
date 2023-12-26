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

        Label(self.root, text="Room Details", font=("times new roman",30, "bold")).place(x=500,y=70, anchor="center")

        buttonFrame = Frame(self.root)
        buttonFrame.place(x=40, y=100, width=140, height=480)

        Button(buttonFrame,text="Single Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.showSingle).pack(padx = 10, pady= 14)
        Button(buttonFrame,text="Double Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.showDouble).pack(padx = 10, pady= 14)
        Button(buttonFrame,text="Triple Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.showTriple).pack(padx = 10, pady=14)
        Button(buttonFrame,text="Quad Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.showQuad).pack(padx = 10, pady= 14)
        Button(buttonFrame,text="Queen Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.showQueen).pack(padx = 10, pady= 14)
        Button(buttonFrame,text="King Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.showKing).pack(padx = 10, pady= 14)
        Button(buttonFrame,text="Twin Room",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.showTwin).pack(padx = 10, pady= 14)
        Button(buttonFrame,text="Suite",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.showSuite).pack(padx = 10, pady= 14)

        self.roomFrame = Frame(self.root,width=770, height=400)
        self.roomFrame.place(x=210, y=125)

        self.showSingle()

        self.root.mainloop()

    def showRoom(self, room_type, image_path, title, size, wifi, bed_size, max_people, room_view, room_price, room_description1,room_description2):
        self.roomFrame = Frame(self.root, width=770, height=400)
        self.roomFrame.place(x=210, y=125)

        self.roomImage = PhotoImage(file=image_path, height=400, width=600)
        Label(self.roomFrame, image=self.roomImage).place(x=0, y=0)

        Label(self.roomFrame, text=title, font=("times new roman", 20, "bold")).place(x=540, y=20)

        self.dimensionFrame = Frame(self.roomFrame, width=160, height=55)
        self.dimensionFrame.place(x=420, y=80)
        self.dimension = PhotoImage(file="Images/Icons/dimensions_icon.png")
        Label(self.dimensionFrame, image=self.dimension).place(x=0, y=0)
        Label(self.dimensionFrame, text=f"Room Size:\n{size}", font=("times new roman", 15, "bold"), fg="black").place(x=55, y=2)

        self.wifiFrame = Frame(self.roomFrame, width=150, height=55)
        self.wifiFrame.place(x=610, y=80)
        self.wifi = PhotoImage(file="Images/Icons/hotel_wifi_icon.png")
        Label(self.wifiFrame, image=self.wifi).place(x=0, y=0)
        Label(self.wifiFrame, text=wifi, font=("times new roman", 15, "bold"), fg="black").place(x=55, y=2)

        Label(self.roomFrame, text=f"Bed Size: {bed_size}", font=("times new roman", 15, "bold")).place(x=420, y=160)
        Label(self.roomFrame, text=f"Max People: {max_people}", font=("times new roman", 15, "bold")).place(x=420, y=200)
        Label(self.roomFrame, text=f"Room View: {room_view}", font=("times new roman", 15, "bold")).place(x=420, y=240)
        Label(self.roomFrame, text=f"Room Price: {room_price}", font=("times new roman", 15, "bold")).place(x=420, y=280)
        Label(self.roomFrame, text="Room Description:", font=("times new roman", 15, "bold")).place(x=420, y=320)
        Label(self.roomFrame, text=room_description1, font=("times new roman", 15, "bold")).place(x=440, y=345)
        Label(self.roomFrame, text=room_description2, font=("times new roman",15, "bold")).place(x=440,y=365)

    def showSingle(self):
        self.showRoom(
            room_type="Single Room",
            image_path="Images/Rooms/Single_Room_1.png",
            title="Single Room",
            size="37m2 to 45m2",
            wifi="Wifi: Yes",
            bed_size="1 Single Bed",
            max_people="1",
            room_view="City View or Ocean View",
            room_price="Rs.10,000",
            room_description1 = "This room is a single room with a single bed." ,
            room_description2 = "It has a nice view and is 37m2 in size."
        )

    def showDouble(self):
        self.showRoom(
            room_type="Double Room",
            image_path="Images/Rooms/Double_Room_1.png",
            title="Double Room",
            size="40m2 to 45m2",
            wifi="Wifi: Yes",
            bed_size="1 Double Bed or 2 Single Beds",
            max_people="2",
            room_view="City View or Ocean View",
            room_price="Rs.15,000",
            room_description1="This room is a double room with two bed options.",
            room_description2="It has a great view and is 40m2 in size."
        )

    # Repeat similar functions for other room types...

    def showTriple(self):
        self.showRoom(
            room_type="Triple Room",
            image_path="Images/Rooms/Triple_Room_1.png",
            title="Triple Room",
            size="45m2 to 65m2",
            wifi="Wifi: Yes",
            bed_size="3 Twin Beds or 1 Double 1 and Twin Bed",
            max_people="3",
            room_view="City View or Ocean View",
            room_price="Rs.20,000",
            room_description1="This room is a triple room with a single beds.",
            room_description2="It has an amazing view and is 45m2 in size."
        )

    #showQuad
    def showQuad(self):
        self.showRoom(
            room_type="Quad Room",
            image_path="Images/Rooms/Quad_Room_1.png",
            title="Quad Room",
            size="70m2 to 85m2",
            wifi="Wifi: Yes",
            bed_size="2 Double Beds",
            max_people="4",
            room_view="City View or Ocean View",
            room_price="Rs.25,000",
            room_description1="This room is a quad room with double beds.",
            room_description2="It has an amazing view and is 70m2 in size."
        )

    #showQueen
    def showQueen(self):
        self.showRoom(
            room_type="Queen Room",
            image_path="Images/Rooms/Queen_Room_1.png",
            title="Queen Room",
            size="32m2 to 50m2",
            wifi="Wifi: Yes",
            bed_size="1 Queen Bed",
            max_people="2",
            room_view="City View or Ocean View",
            room_price="Rs.30,000",
            room_description1="This room is a queen room with a queen bed.",
            room_description2="It has an amazing view and is 40m2 in size."
        )

    #showKing
    def showKing(self):
        self.showRoom(
            room_type="King Room",
            image_path="Images/Rooms/King_Room_1.png",
            title="King Room",
            size="32m2 to 50m2",
            wifi="Wifi: Yes",
            bed_size="1 King Bed",
            max_people="2",
            room_view="City View or Ocean View",
            room_price="Rs.34,000",
            room_description1="This room is a king room with a king bed.",
            room_description2="It has an amazing view and is 40m2 in size."
        )

    #showTwin
    def showTwin(self):
        self.showRoom(
            room_type="Twin Room",
            image_path="Images/Rooms/Twin_Room_1.png",
            title="Twin Room",
            size="32m2 to 40m2",
            wifi="Wifi: Yes",
            bed_size="2 Twin Beds",
            max_people="2",
            room_view="City View or Ocean View",
            room_price="Rs.21,000",
            room_description1="This room is a twin room with two twin beds.",
            room_description2="It has an amazing view and is 40m2 in size."
        )

    #showSuite
    def showSuite(self):
        self.showRoom(
            room_type="Suite Room",
            image_path="Images/Rooms/Suite_Room_1.png",
            title="Suite Room",
            size="50m2 to 70m2",
            wifi="Wifi: Yes",
            bed_size="2 Queen Beds",
            max_people="5",
            room_view="City View or Ocean View",
            room_price="Rs.50,000",
            room_description1="This room is a suite room with two queen beds.",
            room_description2="It has an amazing view and is 70m2 in size."
        )

    def destroyFrame(self):
        self.roomFrame.destroy()

        self.stillFrame = Frame(self.root,width=770, height=500, bg="grey")
        self.stillFrame.place(x=210, y=80)

        Label(self.stillFrame, text="Choose a Room", font=("times new roman",20, "bold")).place(x=340,y=240)

