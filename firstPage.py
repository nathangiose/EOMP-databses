# Nathan John Giose- Group2


# Importing everything from tkinter and messagebox
# Importing a database for mysql


from tkinter import *
from tkinter import messagebox
import pymysql


# WINDOW DESIGN


window = Tk()
window.title("LifeChoices Login")
window.resizable(False, False)
window.geometry("500x500")
window.config(bg="black")

# IMPORTING IMAGE


img = PhotoImage(file="output-onlinejpgtools.png")
canvas = Canvas(window, width=262, height=116)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=126, y=300)


# LABELS


header = Label(window, text="Login", font='Arial 25 bold', bg="black", fg="Green")
header.pack()

username = Label(window, text="Username :", font='Arial 15 bold', bg="black", fg="Green")
username.place(x=60, y=60)

password = Label(window, text="Password :", font='Arial 15 bold', bg="black", fg="Green")
password.place(x=60, y=120)

# Entry Box


user_name = StringVar()
password = StringVar()

userentry = Entry(window, width=35, textvariable=user_name)
userentry.focus()
userentry.place(x=190, y=60)

passentry = Entry(window, width=35, show="*", textvariable=password)
passentry.place(x=190, y=120)


def clear():
	userentry.delete(0, END)
	passentry.delete(0, END)


def close():
	window.destroy()


def login():
	if user_name.get() == "" or password.get() == "":
		messagebox.showerror("Error", "Enter User Name And Password", parent=window)
	else:
		try:
			con = pymysql.connect(host="localhost", user="root", password="", database="docterapp")
			cur = con.cursor()

			cur.execute("select * from user_information where username=%s and password = %s", (user_name.get(), password.get()))
			info = cur.fetchone()

			if info == None:
				messagebox.showerror("Error", "Invalid User Name And Password", parent=window)

			else:
				messagebox.showinfo("Success", "Successfully Login", parent=window)
				close()
				# import new window here
			con.close()
		except Exception as es:
			messagebox.showerror("Error", f"Error Due To : {str(es)}", parent=window)


# button login and clear


btn_login = Button(window, text="Login", bd=4, font='Arial 12 bold', command=login, bg="Black", fg="Green")
btn_login.place(x=190, y=180)


btn_login = Button(window, text="Clear", bd=4, font='Arial 12 bold', command=clear, bg="Green", fg="White")
btn_login.place(x=270, y=180)

window.mainloop()
