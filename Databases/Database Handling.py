import sqlite3

"""
connection = sqlite3.connect("Databases/Hotel_Database.db")
cursorAdm = connection.cursor()  #Creating a cursor to handle database

#cursorAdm.execute('CREATE TABLE Admin_Data ("Admin_ID" text,"Name" text,"Username" text,"Password" text)')
#cursorAdm.execute('insert into Admin_Data values("A00001","Nipun Weerasingha","NipunW","NipunW1!")')

admins=[("A00002","Kyle Peries","KyleP","KyleP2@"),("A00003","Matthew Perera","MatthewP","MattPe3#"),("A00004","Sunil Hevavasam","SunilH","SunilH4$")]
cursorAdm.executemany('insert into Admin_Data values (?,?,?,?)',admins)

connection.commit() #Saving database
connection.close() #Closing datbase
"""