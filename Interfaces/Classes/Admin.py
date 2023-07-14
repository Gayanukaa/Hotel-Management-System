import sqlite3

connection3 = sqlite3.connect("Databases/Hotel_Database.db")
cursorAdm = connection3.cursor()  #Creating a cursor to handle database

#cursorAdm.execute('CREATE TABLE Admin_Data ("Admin_ID" text,"Name" text,"Username" text,"Password" text)')
#cursorAdm.execute('insert into Admin_Data values("A00001","Nipun Weerasingha","NipunW","NipunW1!")')
""" 
admins=[("A00002","Kyle Peries","KyleP","KyleP2@"),("A00003","Matthew Perera","MatthewP","MattPe3#"),("A00004","Sunil Hevavasam","SunilH","SunilH4$")]
cursorAdm.executemany('insert into Admin_Data values (?,?,?,?)',admins)
 """

class Admin:
    def __init__(self):
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

    def run(self):
        print("--------------------Welcome Admin Section--------------------")
        print("____________________Customer Declaration Form____________________")
        print("Any personal data collected on this Form may be used for COVID-19 \nTrack & Trace data processing & record keeping in accordance with\n \t\t    Government Regulations.")
        print("You are declaring on behalf of your entire booking group")

    def validateLogin(username,password):
        msg = ""
        try:
            connection3 = sqlite3.connect("Databases/Hotel_Database.db")
            cursorAdm =connection3.cursor()
            
            data = "Username,Password"
            goal = "Username"
            constrain = username
            
            cursorAdm.execute("select %s from Admin_Data where %s=?" % (data, goal), (constrain,))
            valideData = cursorAdm.fetchall()
            connection3.close()
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

    def getAdminName(username):
        connection3 = sqlite3.connect("Databases/Hotel_Database.db")
        cursorAdm =connection3.cursor()
        data = "Name"
        goal = "Username"
        constrain = username
        cursorAdm.execute("select %s from Admin_Data where %s=?" % (data, goal), (constrain,))
        valideData = cursorAdm.fetchall()
        connection3.close()
        return valideData[0][0]
"""
connection3.commit() #Saving database
connection3.close() #Closing datbase
"""