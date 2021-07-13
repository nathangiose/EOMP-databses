from tkinter import *
import mysql.connector

'''root = Tk()
root.geometry("400x400")
root.title('Life Choices Online')
root.resizable(0, 0)'''


mydb = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='127.0.0.1',
                                   database='LifeChoice_data',
                                   auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
xy = mycursor.execute('Select * from LC')
for i in mycursor:
    print(i)
# root.mainloop()


