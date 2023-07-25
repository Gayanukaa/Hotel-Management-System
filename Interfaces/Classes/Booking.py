import sqlite3
from tkinter import messagebox
from Classes.Customer import Customer
from Classes.Rooms import Rooms

connection3 = sqlite3.connect("Databases/Hotel_Database.db")
cursorBk =connection3.cursor()  #Creating a cursor to handle database

#cursorBk.execute('CREATE TABLE Booking_Details ("Booking_ID" text,"Customer_ID" text,"Name" text,"Room ID" text,"Contact_No" text,"Check_IN" text,"Check_OUT" text,"No_of_Adults" text,"No_of_Children" text,"Price_for_one" text,"RoomNo" text,"Discount" text,"Advance" text,"Total" text,"Meal_Plan" text,"Comment" text)')
#cursorBk.execute('CREATE TABLE Promo_Codes ("PromoCode" text,"Discount" text,"Start_Date" text,"End_Date" text)')
#promotions=[("maxParty10","0.15","01.06.2022","31.06.2022"),("clientJulyDay","0.1","01.07.2022","31.07.2022"),("happyHolidays","0.2","20.07.2022","15.08.2022")]
#cursorBk.executemany('insert into Promo_Codes values (?,?,?,?)',promotions)
#cursorBk.execute('CREATE TABLE Meal_Plan_Criteria ("Meal_Plan" text,"Rate" text)')
#mealPlans=[("Bed and Breakfast","1.0"),("Half Board","1.1"),("Full Board","1.2"),("All Inclusive","1.35")]
#cursorBk.executemany('insert into Meal_Plan_Criteria values (?,?)',mealPlans)

class Booking:
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

    def compareDates(checkIn,checkOut):
        month_in, day_in, year_in = map(int, checkIn.split('/'))
        month_out, day_out, year_out = map(int, checkOut.split('/'))

        if year_out < year_in:
            return False
        elif year_out == year_in and month_out < month_in:
            return False
        elif year_out == year_in and month_out == month_in and day_out < day_in:
            return False
        else:
            return True
    
    def findRoom(checkIn,checkOut,noOfAdults,noOfChildren,mealPlan,childAges):
        # 0<=Age<=6 : No charge
        # 6<Age<=12 : Adult charge/2 
        # Age>12 : Adult

        # Adult rate =room charge /no of persons
        # Total=(Adult rate + meal) * (No of Adult)+ (Adult Rate + meal)/2 * (No of child)+ Additional charge
        # Total bill amount = Total*Discount
        
        roomList=[]

        noOfChildren = 0 if noOfChildren == '' else int(noOfChildren)
        noOfAdults = 0 if noOfAdults == '' else int(noOfAdults)

        connection2 = sqlite3.connect("Databases/Hotel_Database.db")
        cursorBk =connection2.cursor()
        noOfChildren = noOfChildren//2
        total = noOfChildren + noOfAdults
        option = "Capacity"
        cursorBk.execute("select * from Room_Data where %s=?" % (option), (total,))
        roomList = cursorBk.fetchall()
        roomDetails = roomList[0]
        connection2.close()

        price = roomDetails[1]
        roomType = roomDetails[0]

        adultRate = float(price/(noOfAdults+noOfChildren))
        childRate = []
        if (childAges != None):
            for i in childAges:
                if(int(i) <= 6):
                    childRate.append(0)
                elif(int(i) <= 12):
                    childRate.append(adultRate/2)
                else:
                    childRate.append(adultRate)
        else:
            childRate.append(0)

        childPrices = sum(x for x in childRate if isinstance(x, float))
        
        # Meal Plan
        connection2 = sqlite3.connect("Databases/Hotel_Database.db")
        cursorBk =connection2.cursor()
        data = "Rate"
        goal = "Meal_Plan"
        constrain = mealPlan
        cursorBk.execute("select %s from Meal_Plan_Criteria where %s=?" % (data, goal), (constrain,))
        valideData = cursorBk.fetchall()
        mealRate = float(valideData[0][0])
        connection2.close()

        # Total=(Adult rate + meal) * (No of Adult)+ (Adult Rate + meal)/2 * (No of child)+ Additional charge
        total = (adultRate*mealRate) * float(noOfAdults) + (childPrices*mealRate) * float(noOfChildren)

        if(total<price):
            total = price*int(mealRate)
        
        # Total bill amount = Total*Discount
        # Discounts to be implemented

        # Get roomNo for roomType and Available
        connection2 = sqlite3.connect("Databases/Hotel_Database.db")
        cursor =connection2.cursor()
        query = f"SELECT RoomNo FROM Room_Details WHERE Category = ? AND Status = 'Available'"
        # Execute the query with the room type as a parameter
        cursor.execute(query, (roomType,))
        roomNos = cursor.fetchall()
        connection2.close()
        roomNos = roomNos[0]

        advance = 0.4*total

        return [roomType,price,int(total),roomNos,int(advance)]
    
    def createBooking(self,username,roomID,checkIn,checkOut,noOfAdults,noOfChildren,total,roomNo,advance,mealPlan):
        self.username = username
        option = "Username"
        entered = self.username
        try:
            data = Customer.getData(option,entered)
            self.customerID = data[0][0]
            self.name = data[0][1]
            self.contactNo = data[0][5]
        except:
            messagebox.showerror("Error","No data found")

        connection1 = sqlite3.connect("Databases/Hotel_Database.db")
        cursorBk =connection1.cursor()
        cursorBk.execute("SELECT Booking_ID FROM Booking_Details")
        results = cursorBk.fetchall()
        connection1.close()
        final = results[len(results)-1][0]
        self.bookingID = final[0] + str(int(final[1:])+1).zfill(5)

        self.roomID = roomID
        self.checkIn = checkIn
        self.checkOut = checkOut
        self.noOfAdults = int(noOfAdults)
        self.noOfChildren = int(noOfChildren)
        self.total = int(total)
        self.priceForOne = self.total/(self.noOfAdults+self.noOfChildren)
        self.roomNo = roomNo
        self.discount = None
        self.advance = advance
        self.mealPlan = mealPlan
        self.comment = None

        data = [self.bookingID,self.customerID,self.name,self.roomID,self.contactNo,self.checkIn,self.checkOut,self.noOfAdults,self.noOfChildren,self.priceForOne,self.roomNo,self.discount,self.advance,self.total,self.mealPlan,self.comment]
        print(data)

        room = Rooms()
        room.roomNO = roomNo

        cusomter = Customer()
        cusomter.customerID = self.customerID

        customerBooked = cusomter.bookingCompleted(self.customerID)
        try:
            if(customerBooked == False):
                msg = "Error","Customer already booked"
                status = False
            else:
                roomBooked = room.bookRoom(roomNo)
                if(roomBooked == False):
                    msg = "Error","Room already booked"
                    status = False
                else:
                    connection1 = sqlite3.connect("Databases/Hotel_Database.db")
                    cursorBk =connection1.cursor()
                    cursorBk.execute('insert into Booking_Details values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',data)
                    connection1.commit() #Saving database
                    connection1.close() #Closing datbase
                    msg = "Details Entered Successfully \nBookingID: " + self.bookingID
                    status = True
        except Exception:
            msg = str(Exception)
            print(msg)
            status = False

        return status,msg
    
""" 
connection3.commit() #Saving database
connection3.close() #Closing datbase
 """