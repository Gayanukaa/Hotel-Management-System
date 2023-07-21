import sqlite3
from tkinter import messagebox

connection3 = sqlite3.connect("Databases/Hotel_Database.db")
cursorRm =connection3.cursor()  #Creating a cursor to handle database

#cursorBk.execute('CREATE TABLE Booking_Details ("Booking_ID" text,"Customer_ID" text,"Name" text,"Room ID" text,"Contact_No" text,"Check_IN" text,"Check_OUT" text,"No_of_Adults" text,"No_of_Children" text,"Price_for_one" text,"RoomNo" text,"Discount" text,"Advance" text,"Total" text,"Meal_Plan" text,"Comment" text)')
#cursorBk.execute('CREATE TABLE Promo_Codes ("PromoCode" text,"Discount" text,"Start_Date" text,"End_Date" text)')
#promotions=[("maxParty10","0.15","01.06.2022","31.06.2022"),("clientJulyDay","0.1","01.07.2022","31.07.2022"),("happyHolidays","0.2","20.07.2022","15.08.2022")]
#cursorBk.executemany('insert into Promo_Codes values (?,?,?,?)',promotions)
#cursorBk.execute('CREATE TABLE Meal_Plan_Criteria ("Meal_Plan" text,"Rate" text)')
#mealPlans=[("Bed and Breakfast","1.0"),("Half Board","1.1"),("Full Board","1.2"),("All Inclusive","1.35")]
#cursorBk.executemany('insert into Meal_Plan_Criteria values (?,?)',mealPlans)

class Rooms:
    def __init__(self):
        self.roomNO = None
        self.bookingID = None
        self.customerID = None
        self.name = None
        self.roomID = None
        self.contactNo = None
        self.checkIn = None
        self.checkOut = None
        self.noOfAdults = None
        self.noOfChildren = None
        self.priceForOne = None
        self.roomNo = None
        self.discount = None
        self.advance = None
        self.total = None
        self.mealPlan = None
        self.comment = None 
    
    def enterDatatoDatabase(roomNo,category,floor,status,view):
        connection2 = sqlite3.connect("Databases/Hotel_Database.db")
        cursorRm =connection2.cursor()
        option = "RoomNo"
        cursorRm.execute("select * from Room_Details where %s=?" % (option),(roomNo,))
        valideData = cursorRm.fetchall()

        if(len(valideData) == 0):
            print(roomNo,category,floor,status,view)
            data = [roomNo,category,floor,status,view]
            cursorRm.execute('insert into Room_Details values(?,?,?,?,?)',data)
            connection2.commit() #Saving database
            msg = "Details Entered Successfully"
            messagebox.showinfo('message', msg)
            return True
        else:
            msg = "Details Already Exist"
            messagebox.showinfo('message', msg)
            return False

    def getData(entered):
        try:
            connection2 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorRm =connection2.cursor()
            option = "RoomNo"
            cursorRm.execute("select * from Room_Details where %s=?" % (option), (entered,))
            valideData = cursorRm.fetchall()
            #cursorRm.execute("select * from Room_Details where %s=?" % (option), (entered,))
            return valideData
        except sqlite3.Error as error:
            msg = "Details entered not Exist"
            messagebox.showinfo('message', msg)
            return None
        except IndexError as error:
            msg = "Data not matching. Try Again"
            messagebox.showinfo('message', msg)
            return None

    def deleteRoomfromDatabase(entered):
        try:
            connection2 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorRm =connection2.cursor()
            option = "RoomNo"
            cursorRm.execute("delete from Room_Details where %s=?" % (option), (entered,))
            connection2.commit()
            connection2.close()
            msg = "Successfully deleted"
            return msg,True
        except sqlite3.Error as error:
            msg = "Data entered not matching. Try Again"
            return msg,False
        except IndexError as error:
            msg = "Data not matching. Try Again"
            return msg,True

    def getPrice(category):
        try:
            connection2 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorRm =connection2.cursor()
            data = "Charge"
            goal = "Room_Type"
            constrain = category
            cursorRm.execute("select %s from Room_Data where %s=?" % (data, goal), (constrain,))
            valideData = cursorRm.fetchall()
            return valideData[0][0]
        except sqlite3.Error as error:
            return None
        
""" 
connection3.commit() #Saving database
connection3.close() #Closing datbase
 """
"""
cursorRm.execute('insert into Room_Data (View) values("City,Ocean View")')
cursorRm.execute('insert into Room_Data (Rate) values(1.0,1.5)')
"""