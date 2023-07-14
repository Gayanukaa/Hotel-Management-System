from tkinter import *
from tkinter import messagebox
from Classes.CenterFunction import center
from Classes.Customer import Customer

class CustomerProfile:
    def __init__(self,root,username):
        self.root = Toplevel(root)
        self.root.geometry("1000x600")
        self.root.update()
        self.root.title("Customer Profile Page")
        self.root.resizable(False, False)
        center(self.root,1000,600)    

        self.img =  PhotoImage(file="Images/Backgrounds/Gradient_background_7.png")
        Label(self.root, image=self.img).place(x=0, y=0,relwidth=1,relheight=1)
        #self.root.iconbitmap("Images/hnet.com-image.ico")  #For MacOS
        #self.root.iconphoto(False, PhotoImage(file = "Images/hnet.com-image.png")) #For Windows

        self.username = username
        self.newPassword = self.confirmNewPassword = self.oldPassword = ""

        self.searchData()

        if (self.title == "Mr."):
            profile = PhotoImage(file="Images/Icons/male-user-100.png")
        else:
            profile = PhotoImage(file="Images/Icons/female-user-100.png")

        Label(self.root, image=profile,bg="#614385").place(x=450, y=35)

        textIntro = self.title + " " + self.cusname
        Label(self.root,text = textIntro, font=("times new roman",25, "bold"),bg="#614385").place(x=500, y=170, anchor="center")
        Label(self.root,text = self.cusnationality, font=("times new roman",20, "italic")).place(x=500, y=210,anchor="center")

        frame1 = Frame(self.root,bg="grey", width=900, height=120)
        frame1.place(x=50, y = 250)

        Label(frame1,text ="D.O.B : " + self.cusdob, font=('calibre',15,'normal')).place(x=50,y=20)
        Label(frame1,text ="Gender : " + self.gender, font=('calibre',15,'normal')).place(x=300,y=20)
        Label(frame1,text ="ID No. : " + str(self.cusidNo), font=('calibre',15,'normal')).place(x=550,y=20)

        Label(frame1,text ="Contact No. : " + str(self.cuscontactNo), font=('calibre',15,'normal')).place(x=50,y=80)
        Label(frame1,text ="Email : " + self.cusemail, font=('calibre',15,'normal')).place(x=300,y=80)
        Label(frame1,text ="Address : " + self.cusaddress, font=('calibre',15,'normal')).place(x=550,y=80)

        frame2 = Frame(self.root,bg="grey", width=600, height=80)
        frame2.place(x=220, y = 420)

        Label(frame2,text ="Username : " + self.username, font=('calibre',15,'normal')).place(x=30,y=30)
        Label(frame2,text ="Password : " + self.cuspassword, font=('calibre',15,'normal')).place(x=210,y=30)
        Button(frame2,text="Change Password",relief=RAISED,command=self.changePassword).place(x=400,y=30)
        
        self.root.mainloop()
    
    def searchData(self):
        option = "Username"
        entered = self.username

        if(option != None or entered != None):
            data = Customer.getData(option,entered)
            self.cusname = data[0][1]
            self.title = data[0][2]
            self.cusdob = data[0][3]
            self.gender = data[0][4]
            self.cuscontactNo = data[0][5]
            self.cusidNo = data[0][6]
            self.cusemail = data[0][7]
            self.cusnationality = data[0][8]
            self.cusaddress = data[0][9]
            self.username = data[0][10]
            self.cuspassword = data[0][11]
        else:
            messagebox.showerror("Error","Please enter data to search")
    
    def changePassword(self):
        self.chgePwdWindow = Toplevel(self.root)
        self.chgePwdWindow.geometry("500x300")
        center(self.chgePwdWindow,500,300)
        self.root.title("Change Password Window")
        self.root.resizable(False, False)

        Label(self.chgePwdWindow,text="Enter New Password",font=("times new roman",15, "bold")).place(x=50,y=50)
        self.newPwd = Entry(self.chgePwdWindow,text = self.newPassword,font=("times new roman",15, "bold"),show='*')
        self.newPwd.place(x=250,y=50)
        self.newPwd.focus_set()

        Label(self.chgePwdWindow,text="Confirm New Password",font=("times new roman",15, "bold")).place(x=50,y=100)
        self.confnewPwd = Entry(self.chgePwdWindow,text = self.confirmNewPassword,font=("times new roman",15, "bold"),show='*')
        self.confnewPwd.place(x=250,y=100)
        self.confnewPwd.focus_set()

        Label(self.chgePwdWindow,text="Enter Old Password",font=("times new roman",15, "bold")).place(x=50,y=150)
        self.confoldPwd = Entry(self.chgePwdWindow,text = self.oldPassword,font=("times new roman",15, "bold"),show='*')
        self.confoldPwd.place(x=250,y=150)
        self.confoldPwd.focus_set()

        Button(self.chgePwdWindow,text="Submit",relief=RAISED,command=self.submit).place(x=250,y=200)

    def submit(self):
        if(self.newPwd.get() == "" or self.confnewPwd.get() == "" or self.confoldPwd.get() == ""):
            messagebox.showerror("Error","Please enter all fields")
        else:
            if(self.confoldPwd.get() == self.cuspassword):
                if(self.newPwd.get() == self.confnewPwd.get()):
                    status = Customer.updatePassword(self.username,self.newPwd.get())
                    if(status):
                        messagebox.showinfo("Success","Password changed successfully")
                        self.chgePwdWindow.destroy()
                    else:
                        pass
                else:
                    messagebox.showerror("Error","New Password and Confirm New Password do not match")
            else:
                messagebox.showerror("Error","Old Password is incorrect")


