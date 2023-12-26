import itertools
from tkinter import *
import sqlite3
from tkinter import messagebox

connection1 = sqlite3.connect("Databases/Hotel_Database.db")

cursorCus =connection1.cursor()  #Creating a cursor to handle database
#cursorCus.execute('CREATE TABLE Customer_Data ("Customer_ID" text,"Name" text,"Title" text,"Date_of_Birth" text,"Gender" text,"Contact_No" text,"ID_No" int,"Email" text,"Nationality" text,"Address" text,"Username" text,"Password" text,"Status" text)')

class Customer:
    def __init__(self):
        self.customerID = None
        self.name = None
        self.title = None
        self.dob = None
        self.gender = None
        self.contactNo = None
        self.idNo = None
        self.email = None
        self.nationality = None
        self.address = None
        self.username = None
        self.password = None
        self.status = None

    def enterDatatoDatabase(self,name,title,dob,gender,contactNo,idNo,email,nationality,address,username,password):
        connection1 = sqlite3.connect("Databases/Hotel_Database.db")
        cursorCus =connection1.cursor()

        #retrieve data from a specific column
        cursorCus.execute("SELECT Customer_ID FROM Customer_Data")
        results = cursorCus.fetchall()
        final = results[len(results)-1][0]
        customerID = str(int(final[1:])+1).zfill(5)
        self.status = "Registered"

        print(name,title,dob,gender,contactNo,idNo,email,nationality,address,username,password)
        data = [customerID,self.name,self.title,self.dob,self.gender,self.contactNo,self.idNo,self.email,self.nationality,self.address,self.username,self.password,self.status]

        cursorCus.execute('insert into Customer_Data values(?,?,?,?,?,?,?,?,?,?,?,?,?)',data)
        connection1.commit()
        connection1.close() #Closing datbase
        msg = "Details Entered Successfully \nCustomerID: " + customerID
        messagebox.showinfo('message', msg)
        return True

    def validateLogin(username,password):
        msg = ""
        try:
            connection1 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorCus =connection1.cursor()
            data = "Username,Password"
            goal = "Username"
            constrain = username
            cursorCus.execute("select %s from Customer_Data where %s=?" % (data, goal), (constrain,))
            valideData = cursorCus.fetchall()
            data1 = valideData[0][0]
            data2 = valideData[0][1]

            if (data1 == username) and (data2 == password):
                msg = "Successful Login"
                return msg,True
            else:
                msg = "Incorrect Password"
                return msg,False
        except sqlite3.Error as error:
            msg = "Data entered not matching. Try Again"
            return msg,False
        except IndexError as error:
            msg = "Data entered not matching. Try Again"
            return msg,False

    def getCustomerName(username):
        connection1 = sqlite3.connect("Databases/Hotel_Database.db")
        cursorCus =connection1.cursor()
        data = "Name"
        goal = "Username"
        constrain = username
        cursorCus.execute("select %s from Customer_Data where %s=?" % (data, goal), (constrain,))
        valideData = cursorCus.fetchall()
        return valideData[0][0]

    def getNoofCustomers():
        try:
            connection1 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorCus =connection1.cursor()
            data = "Customer_ID"
            goal = "Status"
            constrain = "CheckedIn"
            cursorCus.execute("select %s from Customer_Data where %s=?" % (data, goal), (constrain,))
            valideData1 = cursorCus.fetchall()

            data = "Customer_ID"
            goal = "Status"
            constrain = "Booked"
            cursorCus.execute("select %s from Customer_Data where %s=?" % (data, goal), (constrain,))
            valideData2 = cursorCus.fetchall()

            return (len(valideData1) + len(valideData2))
        except sqlite3.Error as error:
            msg = error
            return msg

    def getData(option,entered):
        try:
            connection1 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorCus =connection1.cursor()
            cursorCus.execute("select * from Customer_Data where %s=?" % (option), (entered,))
            valideData = cursorCus.fetchall()
            connection1.close()
            return valideData
        except sqlite3.Error as error:
            msg = "Details entered not Exist"
            messagebox.showinfo('message', msg)
            return None
        except IndexError as error:
            msg = "Data not matching. Try Again"
            return msg,False

    def updateDatatoDatabase(name,title,dob,gender,contactNo,idNo,email,nationality,address,entered):
        try:
            connection1 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorCus =connection1.cursor()
            sqln = """update Customer_Data set Name = ?,Title = ?,Date_of_Birth = ?,Gender = ?,Contact_No = ?,ID_No = ?,Email = ?,Nationality = ?, Address = ? where Customer_ID = ?"""
            data = [name,title,dob,gender,contactNo,idNo,email,nationality,address,entered]
            #print(data)
            cursorCus.execute(sqln,data)
            connection1.commit()
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

    def deleteCusfromDatabase(option,entered):
        try:
            connection1 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorCus =connection1.cursor()
            cursorCus.execute("delete from Customer_Data where %s=?" % (option), (entered,))
            connection1.commit()
            connection1.close()
            msg = "Successfully deleted"
            return msg,True
        except sqlite3.Error as error:
            msg = "Data entered not matching. Try Again"
            return msg,False
        except IndexError as error:
            msg = "Data not matching. Try Again"
            return msg,False

    def getCustomerInfo(username):
        connection1 = sqlite3.connect("Databases/Hotel_Database.db")
        cursorCus =connection1.cursor()
        data = "*"
        goal = "Username"
        constrain = username
        cursorCus.execute("select %s from Customer_Data where %s=?" % (data, goal), (constrain,))
        valideData = cursorCus.fetchall()
        return valideData

    def updateFromCusProfile(name,title,dob,gender,contactNo,idNo,email,nationality,address,username,password,prevUsername):
        try:
            connection1 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorCus =connection1.cursor()
            sqln = """update Customer_Data set Name = ?,Title = ?,Date_of_Birth = ?,Gender = ?,Contact_No = ?,ID_No = ?,Email = ?,Nationality = ?, Address = ?,Username = ?,Password = ? where Username = ?"""
            data = [name,title,dob,gender,contactNo,idNo,email,nationality,address,username,password,prevUsername]
            cursorCus.execute(sqln,data)
            connection1.commit()
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

    def updatePassword(username,password):
        try:
            connection1 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorCus =connection1.cursor()
            sqln = """update Customer_Data set Password = ? where Username = ?"""
            data = [password,username]
            cursorCus.execute(sqln,data)
            connection1.commit()
            return True
        except sqlite3.Error as error:
            print(error)
            return False
        except IndexError as error:
            print(error)
            return False

    def bookingCompleted(self,customerID):
        try:
            connection1 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorCus =connection1.cursor()
            data = "Status"
            goal = "Customer_ID"
            constrain = customerID
            cursorCus.execute("select %s from Customer_Data where %s=?" % (data, goal), (constrain,))
            valideData = cursorCus.fetchall()
            status = valideData[0][0]

            if(status == "Booked"):
                connection1.close()
                return False
            else:
                sqln = """update Customer_Data set Status = ? where Customer_ID = ?"""
                data = ["Booked",customerID]
                cursorCus.execute(sqln,data)
                connection1.commit()
                connection1.close()
                return True
        except sqlite3.Error as error:
            print(error)
            return False
        except IndexError as error:
            print(error)
            return False

"""
#cursorCus.execute('delete from Customer_Data where Name="Nimal Bandara"')

"""
connection1.commit() #Saving database
connection1.close() #Closing datbase
"""
#cursorCus.execute("update Customer_Data set Name = %s,Title = %s,Date_of_Birth = %s,Gender = %s,Contact_No = %s,ID_No = %s,Email = %s,Nationality = %s, Address = %s where %s=?;" % (name,title,dob,gender,contactNo,idNo,email,nationality,address,option), (entered,))
#sqln = ""#update Customer_Data set Name = ?,Title = ?,Date_of_Birth = ?,Gender = ?,Contact_No = ?,ID_No = ?,Email = ?,Nationality = ?, Address = ? where ?=?"""
