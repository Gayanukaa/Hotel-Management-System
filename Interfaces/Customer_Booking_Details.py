from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from Classes.CenterFunction import center
from Classes.Customer import Customer
from Classes.Booking import Booking

class CusBookDetails:
    def __init__(self,root):
        self.root = Toplevel(root)
        self.root.geometry("1000x600")
        self.root.update()
        self.root.title("Booking Details Page")
        self.root.resizable(False, False)
        center(self.root,1000,600)

        # img =  PhotoImage(file="Images/Backgrounds/Gradient_background_10.png")
        # Label(self.root, image=img).place(x=0, y=0,relwidth=1,relheight=1)

        # self.root.iconbitmap("Images/hnet.com-image.ico")  #For MacOS
        # self.root.iconphoto(False, PhotoImage(file = "Images/hnet.com-image.png")) #For Windows

        Label(self.root,text="Booking Details",font=("times new roman",50,"bold")).place(x=350,y=20)

        frame1 = Frame(self.root)
        frame1.place(x=50, y=100, width=500, height=230)

        '''
        MEAL PLANS
            Category : Single,Double,Triple,Quad,Queen,King,Twin,Suite
            View : City View,Ocean View
            Check IN : 2.00 P.M
            Check OUT : 12.00 P.M
            - Room only
            - Bed and breakfast : 24 hours room/breakfast
            - Half board : 24 hours room/breakfast & lunch
            - Full board : 24 hours / 3 meals
            - All inclusive : 24 hours room/ 3 meals/other
        '''

        Label(frame1,text="Meal Plans",font=("times new roman",20,"bold")).place(x=10,y=10)
        Label(frame1,text="Category : Single,Double,Triple,Quad,Queen,King,Twin,Suite",font=("times new roman",15,"bold")).place(x=30,y=45)
        Label(frame1,text="View : City View,Ocean View",font=("times new roman",15,"bold")).place(x=30,y=65)
        Label(frame1,text="Check IN : 2.00 P.M",font=("times new roman",15,"bold")).place(x=30,y=85)
        Label(frame1,text="Check OUT : 12.00 P.M",font=("times new roman",15,"bold")).place(x=30,y=105)
        Label(frame1,text="- Room only",font=("times new roman",15,"bold")).place(x=50,y=125)
        Label(frame1,text="- Bed and breakfast : 24 hours room/breakfast",font=("times new roman",15,"bold")).place(x=50,y=145)
        Label(frame1,text=" - Half board : 24 hours room/breakfast & lunch",font=("times new roman",15,"bold")).place(x=50,y=165)
        Label(frame1,text="- Full board : 24 hours / 3 meals",font=("times new roman",15,"bold")).place(x=50,y=185)
        Label(frame1,text="- All inclusive : 24 hours room/ 3 meals/other",font=("times new roman",15,"bold")).place(x=50,y=205)

        frame2 = Frame(self.root)
        frame2.place(x=50, y=350, width=250, height=120)

        '''
        CHILD (AGE) POLICY
            0<=Age<=6 : No charge
            6<Age<=12 : Adult charge/2
            Age>12 : Adult
        '''

        Label(frame2,text="Child Age Policy",font=("times new roman",20,"bold")).place(x=10,y=10)
        Label(frame2,text="0<=Age<=6 : No charge",font=("times new roman",15,"bold")).place(x=30,y=45)
        Label(frame2,text="6<Age<=12 : Adult charge/2",font=("times new roman",15,"bold")).place(x=30,y=65)
        Label(frame2,text="Age>12 : Adult charge",font=("times new roman",15,"bold")).place(x=30,y=85)

        """Customer shouldn't allow to cancel a book"""
        Label(self.root,text="Customer are not allowed to cancel a booking",font=("times new roman",20,"bold")).place(x=60,y=500)


        self.root.mainloop()
