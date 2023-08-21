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
        
        img =  PhotoImage(file="Images/Backgrounds/Gradient_background_9.png")
        Label(self.root, image=img).place(x=0, y=0,relwidth=1,relheight=1)

        #self.root.iconbitmap("Images/hnet.com-image.ico")  #For MacOS
        #self.root.iconphoto(False, PhotoImage(file = "Images/hnet.com-image.png")) #For Windows

        
        self.root.mainloop()
