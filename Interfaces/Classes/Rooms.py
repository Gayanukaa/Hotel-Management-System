import sqlite3
from tkinter import messagebox

connection2 = sqlite3.connect("Databases/Hotel_Database.db")
cursorRm =connection2.cursor()  #Creating a cursor to handle database

#cursorRm.execute('CREATE TABLE Room_Data ("Room_Type" text,"Charge" int,"Capacity" int)')
#cursorRm.execute('insert into Room_Data (Room_Type,Charge,Capacity) values("Single",10000,1),("Double",15000,2),("Triple",20000,3),("Quad",25000,4),("Queen",30000,2),("King",34000,2),("Twin",21000,2),("Suite",50000,5)')

#cursorRm.execute('CREATE TABLE Room_Details ("RoomNo" text,"Category" text,"Floor" text,"Status" text,"View" text)')
""" 
rooms=[("410","Twin","4","Available","City View"),
("411","Twin","4","Available","City View"),
("412","Twin","4","Available","Ocean View"),
("413","Twin","4","Available","Ocean View"),
("414","Quad","4","Available","Ocean View"),
("415","Quad","4","Available","Ocean View"),
("416","Queen","4","Available","City View"),
("417","Queen","4","Available","Ocean View"),
("418","Queen","4","Available","Ocean View"),
("419","King","4","Available","Ocean View"),
("420","King","4","Available","City View"),
("421","King","4","Available","City View"),
("422","Suite","4","Available","City View"),
("423","Suite","4","Available","Ocean View"),
("424","Suite","4","Available","Ocean View"),]
cursorRm.executemany('insert into Room_Details values (?,?,?,?,?)',rooms)
 """

class Rooms:
    def __init__(self):
        self.roomNO = None
        self.category = None
        self.floor = None
        self.status = None
        self.view = None
        self.booking = None
    
    def getAvailableRooms():
        connection2 = sqlite3.connect("Databases/Hotel_Database.db")
        cursorRm =connection2.cursor()
        data = "RoomNo"
        goal = "Status"
        constrain = "Available"
        cursorRm.execute("select %s from Room_Details where %s=?" % (data, goal), (constrain,))
        valideData = cursorRm.fetchall()
        return len(valideData)

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

    def updateDatatoDatabase(roomNO,category,floor,status,view,entered):
        try:
            connection2 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorRm =connection2.cursor()
            sqln = """update Room_Details set RoomNo = ?,Category = ?,Floor = ?,Status = ?,View = ? where RoomNo = ?"""
            data = [roomNO,category,floor,status,view,entered]
            #print(data)
            cursorRm.execute(sqln,data)
            connection2.commit()
            msg = "Successfully updated"
            return msg,True
        except sqlite3.Error as error:
            msg = "Data entered not matching. Try Again"
            print(error)
            return msg,False
        except IndexError as error:
            msg = "Data not matching. Try Again"
            print(error)
            return msg,False

    def findPossibleRooms(noOfAdults,noOfChildren):
        try:
            noOfChildren = int(noOfChildren)
            noOfAdults = int(noOfAdults)
            connection2 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorRm =connection2.cursor()
            """ if(noOfChildren % 2 == 0):
                noOfChildren = noOfChildren//2
                total = noOfChildren + noOfAdults
            else:
                total = noOfChildren + noOfAdults """
            noOfChildren = noOfChildren//2
            total = noOfChildren + noOfAdults
            option = "Capacity"
            cursorRm.execute("select * from Room_Data where %s=?" % (option), (total,))
            rooms = cursorRm.fetchall()
            return rooms
        except sqlite3.Error as error:
            return str(error)
        except IndexError as error:
            return str(error)

    def getRate(viewRoom,category):
        try:
            viewRate = 1.1
            print(viewRoom)
            if str(viewRoom) == "City View":
                viewRate = 1.1
            elif str(viewRoom) == "Ocean View":
                viewRate = 1.25
            connection2 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorRm =connection2.cursor()
            option = "Room_Type"
            cursorRm.execute("select Charge from Room_Data where %s=?" % (option), (category,))
            roomBaseRate = cursorRm.fetchall()
            print(roomBaseRate[0][0])
            rate = float(roomBaseRate[0][0]) * viewRate
            return rate
        except sqlite3.Error as error:
            return str(error)
        except IndexError as error:
            return str(error)



""" 
connection2.commit() #Saving database
connection2.close() #Closing datbase
 """
"""
cursorRm.execute('insert into Room_Data (View) values("City,Ocean View")')
cursorRm.execute('insert into Room_Data (Rate) values(1.0,1.5)')
"""