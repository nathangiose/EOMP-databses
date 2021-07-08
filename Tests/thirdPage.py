from tkinter import *
from tkinter import ttk

# Registration GUI design
regiswin = Tk()
regiswin.title("LifeChoices Registration")
regiswin.resizable(False, False)
regiswin.geometry("500x500")
regiswin.config(bg="black")



heading = Label(regiswin , text = "Registration" , font = 'Arial 20 bold', fg="Green", bg="Black")
heading.place(x=80 , y=60)

# form data label
first_name = Label(regiswin, text= "First Name :" , font='Arial 10 bold', fg="Green", bg="Black")
first_name.place(x=80,y=130)

last_name = Label(regiswin, text= "Last Name :" , font='Arial 10 bold', fg="Green", bg="Black")
last_name.place(x=80,y=160)

age = Label(regiswin, text= "Age :" , font='Arial 10 bold', fg="Green", bg="Black")
age.place(x=80,y=190)

Gender = Label(regiswin, text= "Gender :" , font='Arial 10 bold', fg="Green", bg="Black")
Gender.place(x=80,y=220)

city = Label(regiswin, text= "City :" , font='Arial 10 bold', fg="Green", bg="Black")
city.place(x=80,y=260)

add = Label(regiswin, text= "Address :" , font='Arial 10 bold', fg="Green", bg="Black")
add.place(x=80,y=290)

user_name = Label(regiswin, text= "User Name :" , font='Arial 10 bold', fg="Green", bg="Black")
user_name.place(x=80,y=320)

password = Label(regiswin, text= "Password :" , font='Arial 10 bold', fg="Green", bg="Black")
password.place(x=80,y=350)

very_pass = Label(regiswin, text= "Verify Password:" , font='Arial 10 bold', fg="Green", bg="Black")
very_pass.place(x=80,y=380)

# Entry Box


first_name = StringVar()
last_name = StringVar()
age = IntVar(regiswin, value='0')
var= StringVar()
city= StringVar()
add = StringVar()
user_name = StringVar()
password = StringVar()
very_pass = StringVar()


first_name = Entry(regiswin, width=35, textvariable = first_name)
first_name.place(x=200 , y=133)



last_name = Entry(regiswin, width=35, textvariable = last_name)
last_name.place(x=200 , y=163)


age = Entry(regiswin, width=35, textvariable=age)
age.place(x=200 , y=193)


Radio_button_female = ttk.Radiobutton(regiswin,text='Female', value="Female", variable=var).place(x=200, y=220)
Radio_button_male = ttk.Radiobutton(regiswin,text='Male', value="Male", variable=var).place(x=200, y=238)


city = Entry(regiswin, width=35, textvariable=city)
city.place(x=200, y=263)



add = Entry(regiswin, width=35, textvariable=add)
add.place(x=200, y=293)


user_name = Entry(regiswin, width=35, textvariable=user_name)
user_name.place(x=200, y=323)


password = Entry(regiswin, width=35, textvariable=password)
password.place(x=200, y=353)


very_pass= Entry(regiswin, width=35 ,show="*", textvariable=very_pass)
very_pass.place(x=200, y=383)


# button login and clear

btn_signup = Button(regiswin, text = "Register", font='Arial 10 bold')
btn_signup.place(x=200, y=413)


# clear data function
def clear():
    first_name.delete(0,END)
    last_name.delete(0,END)
    age.delete(0,END)
    var.set("Male")
    city.delete(0,END)
    add.delete(0,END)
    user_name.delete(0,END)
    password.delete(0,END)
    very_pass.delete(0,END)


btn_login = Button(regiswin, text="Clear", font='Arial 10 bold', command=clear)
btn_login.place(x=280, y=413)


sign_up_btn = Button(regiswin, text="Go To Login"  )
sign_up_btn.place(x=350, y=20)


regiswin.mainloop()
