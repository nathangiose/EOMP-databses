# Nathan John Giose- Group2


# Importing everything from tkinter and messagebox
# Importing a database for mysql


from tkinter import *
from tkinter import messagebox
import pymysql


# Window Design
win = Tk()
win.title("LifeChoices Login")
win.resizable(False, False)
win.geometry("500x500")
win.config(bg="#202020")


# Heading Label
heading = Label(win, text="Login", font='Arial 25 bold', bg="#202020", fg="Green")
heading.pack()

username = Label(win, text="User Name :", font='Arial 15 bold', bg="#202020", fg="Green")
username.place(x=80, y=60)

userpass = Label(win, text="Password :", font='Arial 15 bold', bg="#202020", fg="Green")
userpass.place(x=80, y=120)

# Entry Box
user_name = StringVar()
password = StringVar()

userentry = Entry(win, width=35, textvariable=user_name)
userentry.focus()
userentry.place(x=200, y=60)

passentry = Entry(win, width=35, show="*", textvariable=password)
passentry.place(x=200, y=120)


def clear():
	userentry.delete(0, END)
	passentry.delete(0, END)

def close():
	win.destroy()


def login():
	if user_name.get() == "" or password.get() == "":
		messagebox.showerror("Error", "Enter User Name And Password", parent=win)
	else:
		try:
			con = pymysql.connect(host="localhost", user="root", password="", database="docterapp")
			cur = con.cursor()

			cur.execute("select * from user_information where username=%s and password = %s", (user_name.get(), password.get()))
			row = cur.fetchone()

			if row==None:
				messagebox.showerror("Error", "Invalid User Name And Password", parent=win)

			else:
				messagebox.showinfo("Success", "Successfully Login", parent=win)
				close()
				#dashboard()
			con.close()
		except Exception as es:
			messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=win)


# button login and clear

btn_login = Button(win, text="Login", font='Arial 12 bold', command=login)
btn_login.place(x=200, y=293)


btn_login = Button(win, text="Clear", font='Arial 12 bold', command=clear)
btn_login.place(x=260, y=293)

win.mainloop()
