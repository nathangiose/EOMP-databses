# Nathan John Giose


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


def update(rows):
    #tv.delete(tv.get_children())
    for i in rows:
        tv.insert('', 'end', values=i)

def search():
    q2 = q.get()
    query = "SELECT ID, name, surname, id_number, phone_number, password, NOK_ID from register where name like '%"+q2+"%' or surname like '%"+q2+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)

def clear():
    query = "SELECT ID, name, surname, id_number, phone_number, password, NOK_ID from register"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)


def getrow():
    return True

# Variables


q = StringVar

# DATABASE CONNECTION


mydb = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC', auth_plugin='mysql_native_password')
cursor = mydb.cursor()



# GUI DESIGN


window = Tk()
window.title("Admin")
window.geometry("700x600")
window.config(bg="Black")
window.resizable(False, False)



# SECTIONING DATA WITH LABELFRAMES


lblframe1 = LabelFrame(window, text="List").pack(fill="both", expand="yes", padx=20, pady=10)
lblframe2 = LabelFrame(window, text="Search").pack(fill="both", expand="yes", padx=20, pady=10)
lblframe3 = LabelFrame(window, text="Users").pack(fill="both", expand="yes", padx=20, pady=10)



# TREE VIEW


tv = ttk.Treeview(lblframe1, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height="5")
tv.pack()


tv.heading(1, text="ID")
tv.heading(2, text="name")
tv.heading(3, text="surname")
tv.heading(4, text="id_number")
tv.heading(5, text="phone_number")
tv.heading(6, text="password")
tv.heading(7, text="NOK_ID")

tv.bind('<Double 1>', command="getrow")


query = "SELECT ID, name, surname, id_number, phone_number, password, NOK_ID from register"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

# SEARCH
searchlbl = Label(lblframe2, text="Search", fg="Green", bg="Black")
searchlbl.pack(side=LEFT, padx=10)
searchent = Entry(lblframe2, textvariable=q)
searchent.pack(side=LEFT, padx=6)
searchbtn = Button(lblframe2, text="Search", command=search)
searchbtn.pack(side=LEFT, padx=6)
cbtnbtn = Button(lblframe2, text="Clear", command=clear)
cbtnbtn.pack(side=LEFT, padx=6)



# USER DATA
userlbl =Label(lblframe3, text="ID")
userlbl.grid(row=0, column=0, padx=5, pady=3)
userent =Entry(lblframe3, textvariable=t1)
userent.grid(row=0, column=1, padx=5, pady=3)

userlbl1 =Label(lblframe3, text="Name")
userlbl1.grid(row=1, column=0, padx=5, pady=3)
userent1 =Entry(lblframe3, textvariable=t2)
userent1.grid(row=1, column=2, padx=5, pady=3)

userlbl2 =Label(lblframe3, text="Surname")
userlbl2.grid(row=2, column=0, padx=5, pady=3)
userent2 =Entry(lblframe3, textvariable=t3)
userent2.grid(row=2, column=3, padx=5, pady=3)

userlbl3 =Label(lblframe3, text4="")
userlbl3.grid(row=3, column=0, padx=5, pady=3)
userent3 =Entry(lblframe3, textvariable=t2)
userent3.grid(row=3, column=4, padx=5, pady=3)

window.mainloop()
