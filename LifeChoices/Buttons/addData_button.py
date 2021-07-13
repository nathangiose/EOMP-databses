from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


# WINDOW DESIGN


test = Tk()
test.title("Admin")
test.resizable(False, False)
test.geometry("500x500")
test.config(bg="black")



# CONNECTING TO THE DATABASE


mydb = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost',
                                   database='LC',
                                   auth_plugin='mysql_native_password')
cursor = mydb.cursor()


# LABLES AND ENTRY BOXES


        lblstudentID = Label(test, font=('Arial', 14, 'bold'), text="Student ID", bd=7)
        lblstudentID.pack()
        entstudentID = Entry(test, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', textvariable=StudentID)
        entstudentID.pack()

        lblname = Label(test, font=('Arial', 14, 'bold'), text="First name", bd=7)
        lblname.pack()
        entname = Entry(test, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', textvariable=name)
        entname.pack()

        lblsurname = Label(test, font=('Arial', 14, 'bold'), text="surname", bd=7)
        lblsurname.pack()
        entsurname = Entry(test, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', textvariable=surname)
        entsurname.pack()

        lblIDnumber = Label(test, font=('Arial', 14, 'bold'), text="ID number", bd=7)
        lblIDnumber.pack()
        entIDnumber = Entry(test, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', textvariable=IDnumber)
        entIDnumber.pack()

        lblphoneNo = Label(test, font=('Arial', 14, 'bold'), text="phone_number", bd=5)
        lblphoneNo.pack()
        entphoneNo = Entry(test, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', textvariable=phoneNo)
        entphoneNo.pack()

        lblNOKname = Label(test, font=('Arial', 14, 'bold'), text="Next of Kin- name", bd=5)
        lblNOKname.pack()
        entNOKname = Entry(test, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', bg="Green", textvariable=NextOfKinname)
        entNOKname.pack()

        lblNOKphoneNo = Label(test, font=('Arial', 14, 'bold'), text="Next of Kin- phoneNo", bd=5)
        lblNOKphoneNo.pack()
        entNOKphoneNo = Entry(test, font=('Arial', 14, 'bold'), bd=5, width=44, justify='left', bg="Green", textvariable=NextOfKinphoneNo)
        entNOKphoneNo.pack()


def addData ():
            if StudentID.get()== "" or name.get()=="" or surname.get()=="" or IDnumber.get()=="" or phoneNo.get()=="" or NextOfKinname.get()=="" or NextOfKinphoneNo.get()=="":
                messagebox.showerror("Administrator", "Please fill in all fields")
            else:
                sqlCon = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost',
                                   database='LC',
                                   auth_plugin='mysql_native_password')
                cur = sqlCon.cursor()
                cur.execute("Insert into LC values(%s, %s, %s, %s, %s, %s, %s)", (
                StudentID.get(),
                name.get(),
                surname.get(),
                IDnumber.get(),
                phoneNo.get(),
                NextOfKinname.get(),
                NextOfKinphoneNo.get(),
                ))
                sqlCon.commit()
                sqlCon.close()
                messagebox.showinfo("Administrator", "Information Updated")


# DECLARING DATA-TYPES
StudentID = StringVar()
name = StringVar()
surname = StringVar()
IDnumber = StringVar()
phoneNo = StringVar()
NextOfKinname = StringVar()
NextOfKinphoneNo = StringVar()


sql = "select * from register"
cursor.execute(sql)
rows = cursor.fetchall()
total = cursor.rowcount

print("Total data Entries: "+ str(total))


frame = Frame(test)
frame.pack(side=LEFT, padx=20)

show = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height="5")
show.pack()


show.heading(1, text="ID")
show.heading(2, text="name")
show.heading(3, text="surname")
show.heading(4, text="id_number")
show.heading(5, text="phone_number")
show.heading(6, text="password")
show.heading(7, text="NOK_ID")

for i in rows:
    show.insert('', 'end', values=i)


btnAddNew = Button(test, font=('Arial', 16, 'bold'), text="Add New", bd=4, pady=1, padx=24, width=8, height=2, command=addData).pack()


test.mainloop()
