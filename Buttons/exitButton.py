from tkinter import *
from tkinter import messagebox


# WINDOW DESIGN


test = Tk()
test.title("Admin")
test.resizable(False, False)
test.geometry("500x500")
test.config(bg="black")

def iExit():
            iExit = messagebox.askyesno("Administrator", "Confirm if you want to exit")
            if iExit > 0:
                test.destroy()
                return

btnExit = Button(test, font=('Arial', 16, 'bold'), text="Exit", bd=4, pady=1, padx=24, width=8,
                                height=2, command=iExit).pack()

test.mainloop()
