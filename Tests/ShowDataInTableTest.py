import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector

win = Tk()
win.title("Admin")
win.geometry("800x500")
win.config(bg="Black")


# IMPORTING IMAGE


img = PhotoImage(file="output-onlinejpgtools.png")
canvas = Canvas(win, width=262, height=116)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=280, y=20)

# DATABASE CONNECTION


mydb = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost',
                                   database='LC',
                                   auth_plugin='mysql_native_password')
cursor = mydb.cursor()


sql = "select * from register"
cursor.execute(sql)
rows = cursor.fetchall()
total = cursor.rowcount

print("Total data Entries: " + str(total))




frame = Frame(win)
frame.place(x=0, y=160)





show = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height="7")
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


win.mainloop()

