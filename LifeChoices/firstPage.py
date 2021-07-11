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

entry_uname = Entry(window, width=35, textvariable=user_name)
entry_uname.focus()
entry_uname.place(x=190, y=60)

entry_pass = Entry(window, width=35, show="*", textvariable=password)
entry_pass.place(x=190, y=120)



# DEFINING BUTTONS


def clear():
	entry_uname.delete(0, END)
	entry_pass.delete(0, END)


def close():
	window.destroy()


def login():
	if user_name.get() == "" or password.get() == "":
		messagebox.showerror("Fill in the spaces", "Please enter a username and password", parent=window)
	else:
		try:
			con = pymysql.connect(host="localhost", user="nathan", password="8-2fermENt2020", database="LifeChoice_data")
			cur = con.cursor()

			cur.execute("select * from user_information where name=%s and ID_No = %s", (user_name.get(), password.get()))
			info = cur.fetchone()

			if info == None:
				messagebox.showerror("Error", "Invalid User Name And Password", parent=window)

			else:
				messagebox.showinfo("Login Successful", "Enjoy your day", parent=window)
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

# EXIT BUTTON


btn_login = Button(window, text="Close", bd=4, font='Arial 12 bold', command=close, bg="Red", fg="Black")
btn_login.place(x=345, y=180)

window.mainloop()
