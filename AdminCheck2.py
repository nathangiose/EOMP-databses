# Nathan John Giose
# First import all the connections we need

from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import mysql.connector


# Creating a class to refer to


class DataBaseConnection:
# INSERT OOP FOR TESTING PURPOSES


    def __init__(self, master):
# GUI DESIGN


        self.master = master
        self.master.geometry("776x700+300+0")
        self.master.title("Administrator")
        self.master.config(bg="Green")
        self.master.resizable(width=False, height=False)

# FRAME THAT HOLDS EVERYTHING
        MainFrame = Frame(self.master, bd=10, width=1350, height=700,  relief=RIDGE, bg="Green")
        MainFrame.grid()


        TitleFrame = Frame(MainFrame, bd=7, width=1340, height=100, bg="Green")
        TitleFrame.grid(row=0, column=0)
        TopFrame3 = Frame(MainFrame, bd=5, width=1340, height=500, relief=RIDGE, bg="Black")
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=1340, height=400, padx=2, bg="Blue", relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, pady=4, relief=RIDGE, bg="Black")
        LeftFrame1.pack(side=TOP, padx=0, pady=0)


        RightFrame1 = Frame(TopFrame3, bd=5, width=320, height=400, padx=2, bg="Red", relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1 ,bd=5, width =310, height=300, padx=2,pady=2 , relief=RIDGE, bg="Black")
        RightFrame1a.pack(side=TOP)

        StudentID =StringVar()
        Firstname =StringVar()
        Surname =StringVar()
        Password =StringVar()
        Role =StringVar()
        Phone =StringVar()

        def addData():
            if StudentID.get() == "" or Firstname.get() == "" or Surname.get() == "":
                tkinter.messagebox.showerror("Enter correct members details")
            else:
                sqlCon = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC', auth_plugin='mysql_native_password')
                cur = sqlCon.cursor()
                cur.execute("Insert into USERS VALUES(%s,%s,%s,%s,%s,%s)", (

                StudentID.get(),
                Firstname.get(),
                Surname.get(),
                Phone.get(),
                Role.get(),
                Password.get(),

                ))

                sqlCon.commit()
                DisplayData()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form", "Record Entered Successfully")


        def DisplayData():
            sqlCon = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC', auth_plugin='mysql_native_password')
            cur = sqlCon.cursor()
            cur.execute("select * from USERS")
            result = cur.fetchall()
            if len(result)!= 0:
                self.student_records.delete(*self.student_records.get_children())
                for row in result:
                        self.student_records.insert('',END,values =row)
                sqlCon.commit()
            sqlCon.close()

        def update():
            sqlCon = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC', auth_plugin='mysql_native_password')
            cur =sqlCon.cursor()
            cur.execute("update USERS set name=%s,surname=%s,password=%s,role=%s,phone=%s where stdid=%s",(

            Firstname.get(),
            Surname.get(),
            Password.get(),
            Role.get(),
            Phone.get(),
            StudentID.get()
            ))
            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Updated")

        def deleteDB():
            sqlCon = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC', auth_plugin='mysql_native_password')
            cur =sqlCon.cursor()
            cur.execute("delete from USERS where stdid=%s",StudentID.get())

            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form","Record Successfully Deleted")
            Reset()


        def searchDB():
            try:
                sqlCon = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC', auth_plugin='mysql_native_password')
                cur = sqlCon.cursor()
                cur.execute("select * from USERS where stdid='%s'"%StudentID.get())

                row = cur.fetchone()

                StudentID.set(row[0])
                Firstname.set(row[1])
                Surname.set(row[2])
                Phone.set(row[3])
                Role.set(row[4])
                Password.set(row[5])

                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("Data Entry Form","No Such Record Found")
                Reset()
            sqlCon.close()

        def Reset():
            self.txtStudentID.delete(0, END)
            self.txtFirstname.delete(0, END)
            self.txtSurname.delete(0, END)
            self.txtPhone.delete(0, END)
            Role.set("")
            self.txtPassword.delete(0, END)

        def iExit():
            iExit =tkinter.messagebox.askyesno("MySql Connection", "Confirm if you want to exit")
            if iExit > 0:
                master.destroy()
                return



        self.lblTitle = Label(TitleFrame, font=('arial', 40, 'bold'), text="Administration", bd=7, bg="Green")
        self.lblTitle.grid(row=0,column=0,  padx=132)

        self.lblStudentID = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Student ID", bd=7, anchor='w', justify=LEFT, fg="Green", bg="Black")
        self.lblStudentID.grid(row=0, column=0, sticky=W, padx=5)
        self.txtStudentID = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable=StudentID)
        self.txtStudentID.grid(row=0, column=1)

        self.lblFirstname = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Firstname", bd=7, anchor='w', justify=LEFT, fg="Green", bg="Black")
        self.lblFirstname.grid(row=1, column=0, sticky=W, padx=5)
        self.txtFirstname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable=Firstname)
        self.txtFirstname.grid(row=1, column=1)

        self.lblSurname = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Surname", bd=7,  justify=LEFT, fg="Green", bg="Black")
        self.lblSurname.grid(row=2, column=0, sticky=W, padx=5)
        self.txtSurname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable=Surname)
        self.txtSurname.grid(row=2, column=1)

        self.lblPhone = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Phone", bd=5, fg="Green", bg="Black")
        self.lblPhone.grid(row=3, column=0, sticky=W, padx=5)
        self.txtPhone = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=Phone)
        self.txtPhone.grid(row=3, column=1, sticky=W)


        self.lblRole = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Role", bd=5, fg="Green", bg="Black")
        self.lblRole.grid(row=4, column=0, sticky=W, padx=5)

        self.cboRole = ttk.Combobox(LeftFrame1, width=42, font=('arial', 12, 'bold'), state='readonly', textvariable=Role)
        self.cboRole['values'] = ('', 'Student', 'Lecturer')
        self.cboRole.current(0)
        self.cboRole.grid(row=4, column=1)

        self.lblPassword = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Password", bd=7, fg="Green", bg="Black")
        self.lblPassword.grid(row=5, column=0, sticky=W, padx=5)
        self.txtPassword = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable=Password, show="*")
        self.txtPassword.grid(row=5, column=1)




        scroll_x = Scrollbar(LeftFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)

        self.student_records = ttk.Treeview(LeftFrame, height=12, columns=("stdid", "firstname", "surname", "phone",
        "role", "password"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.student_records.heading("stdid", text="StudentID.")
        self.student_records.heading("firstname", text="Firstname")
        self.student_records.heading("surname", text="Surname")
        self.student_records.heading("password", text="Password")
        self.student_records.heading("role", text="Role")
        self.student_records.heading("phone", text="Phone")

        self.student_records['show'] = 'headings'

        self.student_records.column("stdid", width=70)
        self.student_records.column("firstname", width=100)
        self.student_records.column("surname", width=100)
        self.student_records.column("password", width=100)
        self.student_records.column("role", width=70)
        self.student_records.column("phone", width=70)

        self.student_records.pack(fill=BOTH, expand=1)
        self.student_records.bind("<ButtonRelease-1>")
        #DisplayData() # This will keep the data showing


        self.btnAddNew = Button(RightFrame1a, pady=1, bd=4, fg="Green", bg="Black", font=('arial', 16,'bold'), padx=24,
                            width=8, height=2, text="Add New Data", command=addData).grid(row=0, column=0, padx=1)

        self.btnDisplay = Button(RightFrame1a, pady=1, bd=4, fg="Green", bg="Black", font=('arial', 16, 'bold'), padx=24,
                            width=8, height=2, text="Display", command=DisplayData).grid(row=1, column=0,padx=1)

        self.btnUpdate = Button(RightFrame1a, pady=1, bd=4, fg="Green", bg="Black", font=('arial', 16, 'bold'), padx=24,
                            width=8, height=2, text="Update", command=update).grid(row=2, column=0, padx=1)

        self.btnDelete = Button(RightFrame1a, pady=1, bd=4, fg="Green", bg="Black", font=('arial', 16, 'bold'), padx=24,
                    width=8, height=2, text="Delete", command=deleteDB).grid(row=3, column=0, padx=1)


        self.btnSearch = Button(RightFrame1a, pady=1, bd=4, fg="Green", bg="Black", font=('arial', 16,'bold'), padx=24,
                            width=8, height=2, text="Search", command=searchDB).grid(row=4, column=0, padx=1)

        self.btnReset = Button(RightFrame1a, pady=1, bd=4, fg="Green", bg="Black", font=('arial', 16, 'bold'), padx=24,
                            width=8, height=2, text="Reset", command=Reset).grid(row=5, column=0, padx=2)

        self.btnExit = Button(RightFrame1a, pady=1, bd=4, fg="Green", bg="Black", font=('arial', 16, 'bold'), padx=24,
                    width=8, height=2, text='Exit', command=iExit).grid(row=6, column=0, padx=1)


if __name__ == '__main__':
    master = Tk()
    application = DataBaseConnection(master)
    master.mainloop()
