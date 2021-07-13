from tkinter import *
from tkinter import ttk
import tkinter.messagebox
#import mysql.connector
import mysql.connector
# import doctest

class ConnectorDB:

    def __init__(self, master):
        self.master = master
        titlespace = " "
        self.master.title("Administrator")
        self.master.geometry("1000x700")
        self.master.resizable(width=False, height=False)

        MainFrame = Frame(self.master, bd=10, width=770, height=700, relief=RIDGE, bg="Black")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=8, width=770, height=100, relief=RIDGE, bg="Green")
        TitleFrame.grid(row=0, column=0)
        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, relief=RIDGE, bg="#208020", padx=2)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, relief=RIDGE, padx=2, pady=4)
        LeftFrame1.pack(side=TOP, padx=0, pady=0)

        RightFrame = Frame(TopFrame3, bd=5, width=100, height=400, relief=RIDGE, bg="#208020", padx=2)
        RightFrame.pack(side=RIGHT)
        RightFrame1 = Frame(RightFrame, bd=5, width=90, height=300, relief=RIDGE, padx=2, pady=2)
        RightFrame1.pack(side=TOP)

        # DECLARING VARIABLES
        ID = StringVar()
        name = StringVar()
        surname = StringVar()
        id_number = StringVar()
        phone_number = StringVar()
        NextOfKinname = StringVar()
        NextOfKinphoneNo = StringVar()

        # DEF VARIABLES


        def addData ():
            if ID.get() == "" or name.get() == "" or surname.get() == "" or id_number.get() == "" or phone_number.get() == "":
                tkinter.messagebox.showerror("Administrator", "Please fill in all fields")
            else:
                sqlCon = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost',
                                   database='LC',
                                   auth_plugin='mysql_native_password')
                cur = sqlCon.cursor()
                cur.execute("Insert into register values('ID', 'name', 'surname', 'id_number', 'phone_number', 'password')", (
                ID.get(),
                name.get(),
                surname.get(),
                id_number.get(),
                phone_number.get(),
                ))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Administrator", "Information Updated")

        def DisplayData():
                sqlCon = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost',
                                   database='LC',
                                   auth_plugin='mysql_native_password')
                cur = sqlCon.cursor()
                cur.execute("select from register")
                result = cur.fetchall()
                if len(result):
                    self.student_records.delete(*self.student_records.get_children())
                    for row in result:
                        self.student_records.insert('', END, values=row)
                sqlCon.commit()
                sqlCon.close()
                #tkinter.messagebox.showinfo("Administrator", "Information Updated")

        def TraineeInfo (ev):
            viewInfo=self.student_records.focus()
            learnerData = self.student_records.item(viewInfo)
            row = learnerData['values']
            ID.set(row[0])
            name.set(row[1])
            surname.set(row[2])
            id_number.set(row[3])
            phone_number.set(row[4])
            NextOfKinname.set(row[5])
            NextOfKinphoneNo.set(row[6])

        def update():
            sqlCon = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost',
                                   database='LC',
                                   auth_plugin='mysql_native_password')
            cur = sqlCon.cursor()
            cur.execute("update register set name%s, surname%s, id_number%s, phone_number%s, NOK-name%s, NOK-phone_number%s, where ID%s)", (
                ID.get(),
                name.get(),
                surname.get(),
                id_number.get(),
                phone_number.get(),
                NextOfKinname.get(),
                NextOfKinphoneNo.get(),
            ))
            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Administrator", "Information Updated")


        def deleteDB():
            sqlCon = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost',
                                   database='LC',
                                   auth_plugin='mysql_native_password')
            cur = sqlCon.cursor()
            cur.execute("Delete from register where ID%s", ID.get())

            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Administrator", "Information Deleted")
            Reset()

        def searchDB():
            try:
                sqlCon = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost',
                                   database='LC',
                                   auth_plugin='mysql_native_password')
                cur = sqlCon.cursor()
                cur.execute("Select * from LC where ID%s", ID.get())

                row = cur.fetchall()

                ID.set(row[0])
                name.set(row[1])
                surname.set(row[2])
                id_number.set(row[3])
                phone_number.set(row[4])
                NextOfKinname.set(row[5])
                NextOfKinphoneNo.set(row[6])

                sqlCon.commit()
                DisplayData()
            except:
                tkinter.messagebox.showinfo("Administrator", "Record not Found")
                Reset()
            sqlCon.close()


        def Reset ():
            self.entstudentID.delete(0, END)
            self.entname.delete(0, END)
            self.entsurname.delete(0, END)
            self.entIDnumber.delete(0, END)
            self.entphoneNo.delete(0, END)
            self.entNOKname.delete(0, END)
            self.entNOKphoneNo.delete(0, END)


        def iExit ():
            iExit = tkinter.messagebox.askyesno("Administrator", "Confirm if you want to exit")
            if iExit > 0:
                master.destroy()
                return




        # WIDGETS


        self.lbltitle = Label (TitleFrame, font=('Arial', 40, 'bold'), text="Administrator", bd=7, bg="Green")
        self.lbltitle.grid(row=0, column=0, padx=132)

        self.lblstudentID = Label(LeftFrame1, font=('Arial', 14, 'bold'), text="Student ID", bd=7)
        self.lblstudentID.grid(row=1, column=0, sticky=W, padx=5)
        self.entstudentID = Entry(LeftFrame1, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', textvariable=ID)
        self.entstudentID.grid(row=1, column=1, sticky=W, padx=5)

        self.lblname = Label(LeftFrame1, font=('Arial', 14, 'bold'), text="First name", bd=7)
        self.lblname.grid(row=2, column=0, sticky=W, padx=5)
        self.entname = Entry(LeftFrame1, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', textvariable=name)
        self.entname.grid(row=2, column=1, sticky=W, padx=5)

        self.lblsurname = Label(LeftFrame1, font=('Arial', 14, 'bold'), text="surname", bd=7)
        self.lblsurname.grid(row=3, column=0, sticky=W, padx=5)
        self.entsurname = Entry(LeftFrame1, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', textvariable=surname)
        self.entsurname.grid(row=3, column=1, sticky=W, padx=5)

        self.lblIDnumber = Label(LeftFrame1, font=('Arial', 14, 'bold'), text="ID number", bd=7)
        self.lblIDnumber.grid(row=4, column=0, sticky=W, padx=5)
        self.entIDnumber = Entry(LeftFrame1, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', textvariable=id_number)
        self.entIDnumber.grid(row=4, column=1, sticky=W, padx=5)

        self.lblphoneNo = Label(LeftFrame1, font=('Arial', 14, 'bold'), text="phone_number", bd=5)
        self.lblphoneNo.grid(row=5, column=0, sticky=W, padx=5)
        self.entphoneNo = Entry(LeftFrame1, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', textvariable=phone_number)
        self.entphoneNo.grid(row=5, column=1, sticky=W, padx=5)

        self.lblNOKname = Label(LeftFrame1, font=('Arial', 14, 'bold'), text="Next of Kin- name", bd=5)
        self.lblNOKname.grid(row=6, column=0, sticky=W, padx=5)
        self.entNOKname = Entry(LeftFrame1, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', bg="Green", textvariable=NextOfKinname)
        self.entNOKname.grid(row=6, column=1, sticky=W, padx=5)

        self.lblNOKphoneNo = Label(LeftFrame1, font=('Arial', 14, 'bold'), text="Next of Kin- phone_number", bd=5)
        self.lblNOKphoneNo.grid(row=7, column=0, sticky=W, padx=5)
        self.entNOKphoneNo = Entry(LeftFrame1, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', bg="Green", textvariable=NextOfKinphoneNo)
        self.entNOKphoneNo.grid(row=7, column=1, sticky=W, padx=5)

        # TREE VIEW


        scroll_y = Scrollbar(LeftFrame, orient = VERTICAL)
        self.student_records = ttk.Treeview(LeftFrame, height=12, columns=("ID", "name", "surname", "id_number", "phone_number", "NOK-name", "NOK-phone_number"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)


        self.student_records.heading("ID", text="Student ID")
        self.student_records.heading("name", text="name")
        self.student_records.heading("surname", text="surname")
        self.student_records.heading("id_number", text="ID Number")
        self.student_records.heading("phone_number", text="phone_number")
        self.student_records.heading("NOK-name", text="NOK-name")
        self.student_records.heading("NOK-phone_number", text="NOK-phone_number")

        #self.student_records['tv'] = 'headings'

        self.student_records.column("ID", width=70)
        self.student_records.column("name", width=100)
        self.student_records.column("surname", width=100)
        self.student_records.column("id_number", width=100)
        self.student_records.column("phone_number", width=70)
        self.student_records.column("NOK-name", width=100)
        self.student_records.column("NOK-phone_number", width=70)
        self.student_records.pack(fill=BOTH, expand=1)

        self.student_records.bind("<ButtonRelease-1>", TraineeInfo)
        #DisplayData() #This keeps the data visble, and overrides the button


        # BUTTONS


        self.btnAddNew= Button(RightFrame1, font=('Arial', 16, 'bold'), text="Add New", bd=4, pady=1, padx=24, width=8, height=2, command=addData).grid(row=0, column=0, padx=1)

        self.btnDisplay = Button(RightFrame1, font=('Arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24, width=8,
                                height=2, command=DisplayData).grid(row=1, column=0, padx=1)

        self.btnUpdate = Button(RightFrame1, font=('Arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24, width=8,
                                height=2, command=update).grid(row=2, column=0, padx=1)

        self.btnDelete = Button(RightFrame1, font=('Arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24, width=8,
                                height=2, command=deleteDB).grid(row=3, column=0, padx=1)

        self.btnSearch = Button(RightFrame1, font=('Arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24, width=8,
                                height=2, command=searchDB).grid(row=4, column=0, padx=1)

        self.btnReset = Button(RightFrame1, font=('Arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24, width=8,
                                height=2, command=Reset).grid(row=5, column=0, padx=1)

        self.btnExit = Button(RightFrame1, font=('Arial', 16, 'bold'), text="Exit", bd=4, pady=1, padx=24, width=8,
                                height=2, command=iExit).grid(row=6, column=0, padx=1)



if __name__=='__main__':
    master = Tk()
    application = ConnectorDB(master)
    master.mainloop()
