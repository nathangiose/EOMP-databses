from tkinter import*
from tkinter import ttk
import tkinter.messagebox
#import pymysql
import mysql.connector



class ConnectorDB:

    def __init__(self,root):
        self.root = root
        blank_space = " "
        self.root.title(102 * blank_space + "MySql Connector")
        self.root.resizable(width =False, height=False)
        self.root.geometry("776x700+300+0")

        MainFrame = Frame(self.root ,bd=10, width =1350, height=700,  relief=RIDGE, bg="cadet blue" )
        MainFrame.grid()


        TitleFrame = Frame(MainFrame ,bd=7, width =1340, height=100 ,relief=RIDGE)
        TitleFrame.grid(row = 0 ,column = 0)
        TopFrame3 = Frame(MainFrame ,bd=5, width =1340, height=500 ,relief=RIDGE)
        TopFrame3.grid(row = 1 ,column = 0)

        LeftFrame = Frame(TopFrame3 ,bd=5, width =1340, height=400, padx=2,bg="cadet blue" ,relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame ,bd=5, width =600, height=180, padx=2,pady=4,relief=RIDGE)
        LeftFrame1.pack(side=TOP,padx=0,pady=0)


        RightFrame1 = Frame(TopFrame3 ,bd=5, width =320, height=400, padx=2, bg="cadet blue" , relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1 ,bd=5, width =310, height=300, padx=2,pady=2 , relief=RIDGE)
        RightFrame1a.pack(side=TOP)




        StudentID =StringVar()
        Firstname =StringVar()
        Surname =StringVar()
        Address =StringVar()
        Gender =StringVar()
        Mobile =StringVar()


        def iExit():
            iExit =tkinter.messagebox.askyesno("MySql Connection", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            self.txtStudentID.delete(0,END)
            self.txtFirstname.delete(0,END)
            self.txtSurname.delete(0,END)
            self.txtAddress.delete(0,END)
            Gender.set("")
            self.txtMobile.delete(0,END)


        def addData():
            if StudentID.get() =="" or Firstname.get()=="" or Surname.get()=="" :
                tkinter.messagebox.showerror("Enter correct members details")
            else:
                sqlCon =mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC_online', auth_plugin='mysql_native_password')
                cur =sqlCon.cursor()
                cur.execute("insert into trainee values(%s,%s,%s,%s,%s,%s)",(

                StudentID.get(),
                Firstname.get(),
                Surname.get(),
                Address.get(),
                Gender.get(),
                Mobile.get(),

                ))

                sqlCon.commit()
                DisplayData()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form","Record Entered Successfully")


        def DisplayData():
            sqlCon = mysql.connector.connect(host ="localhost",user="root",password="CkerryCCC",database="trainee")
            cur = sqlCon.cursor()
            cur.execute("select * from trainee")
            result = cur.fetchall()
            if len(result)!= 0:
                self.student_records.delete(*self.student_records.get_children())
                for row in result:
                        self.student_records.insert('',END,values =row)
                sqlCon.commit()
            sqlCon.close()

        def TraineeInfo(ev):
            viewInfo = self.student_records.focus()
            learnerData = self.student_records.item(viewInfo)
            row = learnerData['values']
            StudentID.set(row[0])
            Firstname.set(row[1])
            Surname.set(row[2])
            Address.set(row[3])
            Gender.set(row[4])
            Mobile.set(row[5])


        def update():
            sqlCon =mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC_online', auth_plugin='mysql_native_password')
            cur =sqlCon.cursor()
            cur.execute("update trainee set firstname=%s,surname=%s,address=%s,gender=%s,mobile=%s where stdid=%s",(

            Firstname.get(),
            Surname.get(),
            Address.get(),
            Gender.get(),
            Mobile.get(),
            StudentID.get()
            ))
            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form","Record Successfully Updated")

        def deleteDB():
            sqlCon =mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC_online', auth_plugin='mysql_native_password')
            cur =sqlCon.cursor()
            cur.execute("delete from trainee where stdid=%s",StudentID.get())

            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form","Record Successfully Deleted")
            Reset()



        def searchDB():
            try:
                sqlCon = mysql.connector.connect(host ="localhost",user="root",password="CkerryCCC",database="trainee")
                cur = sqlCon.cursor()
                cur.execute("select * from trainee where stdid='%s'"%StudentID.get())

                row = cur.fetchone()

                StudentID.set(row[0])
                Firstname.set(row[1])
                Surname.set(row[2])
                Address.set(row[3])
                Gender.set(row[4])
                Mobile.set(row[5])


                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("Data Entry Form","No Such Record Found")
                Reset()
            sqlCon.close()

        self.lblTitle = Label(TitleFrame, font=('arial',40, 'bold'),text="MySql Connection",bd=7)
        self.lblTitle.grid(row=0,column=0,  padx=132)

        self.lblStudentID = Label(LeftFrame1, font=('arial',12, 'bold'),text="Student ID",bd=7, anchor='w',justify=LEFT)
        self.lblStudentID.grid(row=0,column=0, sticky =W, padx=5)
        self.txtStudentID = Entry(LeftFrame1,font=('arial', 12,'bold'), bd=5, width=44,justify = 'left',textvariable=StudentID)
        self.txtStudentID.grid(row=0,column=1)

        self.lblFirstname = Label(LeftFrame1, font=('arial',12, 'bold'),text="Firstname", bd=7, anchor='w',justify=LEFT)
        self.lblFirstname.grid(row=1,column=0, sticky =W, padx=5)
        self.txtFirstname = Entry(LeftFrame1,font=('arial', 12,'bold'), bd=5, width=44,justify = 'left',textvariable=Firstname)
        self.txtFirstname.grid(row=1,column=1)

        self.lblSurname = Label(LeftFrame1, font=('arial',12, 'bold'),text="Surname",bd=7,  justify=LEFT)
        self.lblSurname.grid(row=2,column=0, sticky =W, padx=5)
        self.txtSurname = Entry(LeftFrame1,font=('arial', 12,'bold'), bd=5, width=44,justify = 'left',textvariable=Surname)
        self.txtSurname.grid(row=2,column=1)

        self.lblAddress = Label(LeftFrame1, font=('arial',12, 'bold'),text="Address", bd=7, )
        self.lblAddress.grid(row=3,column=0, sticky =W, padx=5)
        self.txtAddress = Entry(LeftFrame1,font=('arial', 12,'bold'), bd=5, width=44,justify = 'left', textvariable=Address)
        self.txtAddress.grid(row=3,column=1)



        self.lblGender = Label(LeftFrame1, font=('arial',12, 'bold'),text="Gender ", bd=5, )
        self.lblGender.grid(row=4,column=0, sticky =W, padx=5)

        self.cboGender=ttk.Combobox(LeftFrame1, width=42 , font=('arial',12,'bold'),state='readonly',textvariable=Gender)
        self.cboGender['values'] =('','Female','Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=4,column=1)


        self.lblMobile = Label(LeftFrame1, font=('arial',12, 'bold'),text="Mobile ", bd=5 )
        self.lblMobile.grid(row=5,column=0 , sticky =W, padx=5)
        self.txtMobile = Entry(LeftFrame1,font=('arial', 12,'bold'), bd=5, width=44,textvariable=Mobile)
        self.txtMobile.grid(row=5,column=1, sticky =W)



        scroll_x=Scrollbar(LeftFrame,orient=HORIZONTAL)
        scroll_y=Scrollbar(LeftFrame,orient=VERTICAL)

        self.student_records=ttk.Treeview(LeftFrame,height=12,columns=("stdid","firstname","surname","address",
        "gender","mobile"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.student_records.heading("stdid",text="StudentID.")
        self.student_records.heading("firstname",text="Firstname")
        self.student_records.heading("surname",text="Surname")
        self.student_records.heading("address",text="Address")
        self.student_records.heading("gender",text="Gender")
        self.student_records.heading("mobile",text="Mobile")

        self.student_records['show']='headings'

        self.student_records.column("stdid", width=70)
        self.student_records.column("firstname",width=100)
        self.student_records.column("surname",width=100)
        self.student_records.column("address",width=100)
        self.student_records.column("gender",width=70)
        self.student_records.column("mobile",width=70)

        self.student_records.pack(fill=BOTH,expand=1)
        self.student_records.bind("<ButtonRelease-1>",TraineeInfo)
        DisplayData()


        self.btnAddNew=Button(RightFrame1a,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),padx=24,
                            width=8,height=2,text="Add New Data",command=addData).grid(row=0, column=0,padx=1)

        self.btnDisplay=Button(RightFrame1a,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),padx=24,
                            width=8,height=2,text="Display",command=DisplayData).grid(row=1, column=0,padx=1)

        self.btnUpdate=Button(RightFrame1a,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),padx=24,
                            width=8,height=2,text="Update",command=update).grid(row=2, column=0,padx=1)

        self.btnDelete=Button(RightFrame1a,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),padx=24,
                    width=8,height=2, text="Delete",command=deleteDB).grid(row=3, column=0,padx=1)


        self.btnSearch=Button(RightFrame1a,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),padx=24,
                            width=8,height=2,text="Search" ,command=searchDB).grid(row=4, column=0,padx=1)

        self.btnReset=Button(RightFrame1a,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),padx=24,
                            width=8,height=2,text="Reset",command=Reset).grid(row=5, column=0,padx=2)

        self.btnExit=Button(RightFrame1a,pady=1, bd=4, fg="black",font=('arial', 16,'bold'),padx=24,command=iExit,
                    width=8, height=2,text='Exit').grid(row=6, column=0, padx=1)


if __name__ == '__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()
