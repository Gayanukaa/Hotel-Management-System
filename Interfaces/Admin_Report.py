import sqlite3
from tkinter import *
from tkinter import ttk
from Classes.CenterFunction import center
from reportlab.pdfgen import canvas
class AdminReport:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1000x600")
        self.root.update()
        self.root.title("Admin Booking Report")
        self.root.resizable(False, False)
        center(self.root,1000,600)

        img = PhotoImage(file="Images/Backgrounds/Gradient_background_2.png")
        Label(self.root,image=img).place(x=0,y=0,relwidth=1,relheight=1)

        #self.root.iconbitmap("Images/hnet.com-image.ico")  #For MacOS
        #self.root.iconphoto(False, PhotoImage(file = "Images/hnet.com-image.png")) #For Windows

        Label(self.root,text ="Booking Report",font=('calibre',25,'normal')).place(x=400,y=30)

        data = self.fetch_data_from_database()

        frame = Frame(self.root, bg="grey")
        frame.place(x=100, y=100, width=800, height=400)

        tree = ttk.Treeview(frame)
        tree["columns"] = ("Booking ID", "Customer ID", "Name", "Check In", "Check Out", "No. of Adults", "No. of Child", "Meal Plan", "Room ID", "Total")

        tree.column("#0", width=0, stretch=NO)
        for col in tree["columns"]:
            tree.column(col, anchor=CENTER)
            tree.heading(col, text=col, anchor=CENTER)

        vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        vsb.pack(side="right", fill="y")
        tree.configure(yscrollcommand=vsb.set)

        hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
        hsb.pack(side="bottom", fill="x")
        tree.configure(xscrollcommand=hsb.set)

        for row in data:
            tree.insert("", END, values=row)

        tree.pack(expand=True, fill="both")

        Button(self.root,text="Printed",relief=RAISED,borderwidth=3,font=("times new roman",15,"bold"),command=self.export_to_pdf(tree)).place(x=450,y=550)

        self.root.mainloop()


    def fetch_data_from_database(self):
        connection = sqlite3.connect("Databases/Hotel_Database.db")
        cursor = connection.cursor()

        cursor.execute("SELECT Booking_ID, Customer_ID, Name, Check_IN, Check_OUT, No_of_Adults, No_of_Children, Meal_Plan, RoomNo, Total FROM Booking_Details")
        data = cursor.fetchall()
        connection.close()

        return data

    def export_to_pdf(self,tree):
        pdf_filename = "Booking_Report.pdf"
        c = canvas.Canvas(pdf_filename, pagesize=(1000, 500))
        width, height = 1000, 500
        x_offset = 50
        y_offset = height - 50

        for col, col_name in enumerate(tree["columns"]):
            c.drawString(x_offset + col * 100, y_offset, col_name)
            for row, item in enumerate(tree.get_children()):
                c.drawString(x_offset + col * 100, y_offset - (row + 1) * 20, tree.item(item, 'values')[col])

        c.save()
