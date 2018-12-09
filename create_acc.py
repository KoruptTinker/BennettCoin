import tkinter as tk
from tkinter import *

import sqlite3
conn = sqlite3.connect('new.db')
c=conn.cursor()
def ca_window():
    #creating window
    creation_window=tk.Tk()
    creation_window.title("Create an account")

    #functions

    def store_variables():
        #variables to be put  in database
        #global ca_option1, ca_option2, ca_option3, ca_option3_1, ca_option4
        user=ca_entry1.get()
        password=ca_entry2.get()
        full_name=ca_entry3.get()
        e_roll=ca_entry3_1.get()
        course=ca_entry4.get()
        #Creating a table
        conn = sqlite3.connect('new.db')
        c=conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS users(Unique_ID INTEGER PRIMARY KEY AUTOINCREMENT,Username text NOT NULL,Password text NOT NULL, Full_Name text NOT NULL, Enrollment_No text NOT NULL, Course text NOT NULL, Face integer NULL, Balance REAL NOT NULL, Total_Expenditure REAL NOT NULL)")
        conn.commit()
        
        #adding data
        c.execute("INSERT INTO users(Username, Password, Full_Name, Enrollment_No, Course, Face, Balance, Total_Expenditure) VALUES(?,?,?,?,?,?,?,?)",(user,password,full_name,e_roll,course,"",0,0))
        conn.commit()
    def SetToZero():
        ca_entry1.delete('0', END)
        ca_entry2.delete('0', END)
        ca_entry3.delete('0', END)
        ca_entry3_1.delete('0', END)
        ca_entry4.delete('0', END)
        
            
        
        

    #main body
    ca_header= Label(creation_window, text="Create an account")
    ca_header.config(font=("Ariel", 20))
    ca_header.grid(row=0, column=0, columnspan=2)
    
    ca_option1= Label(creation_window, text="Username:")
    ca_option1.config(font=("Ariel", 10))
    ca_option1.grid(row=1, column=0)

    ca_entry1= Entry(creation_window)
    ca_entry1.grid(row=1, column=1)

    ca_option2= Label(creation_window, text="Password:")
    ca_option2.config(font=("Ariel", 10))
    ca_option2.grid(row=2, column=0)

    ca_entry2= Entry(creation_window, show="*")
    ca_entry2.grid(row=2, column=1)

    ca_option3= Label(creation_window, text="Full Name:")
    ca_option3.config(font=("Ariel", 10))
    ca_option3.grid(row=3, column=0)

    ca_entry3= Entry(creation_window)
    ca_entry3.grid(row=3, column=1)

    ca_option3_1= Label(creation_window, text="Enrollment Number:")
    ca_option3_1.config(font=("Ariel", 10))
    ca_option3_1.grid(row=4, column=0)

    ca_entry3_1= Entry(creation_window)
    ca_entry3_1.grid(row=4, column=1)

    ca_option4= Label(creation_window, text="Course:")
    ca_option4.config(font=("Ariel", 10))
    ca_option4.grid(row=5, column=0)

    ca_entry4= Entry(creation_window)
    ca_entry4.grid(row=5, column=1)

    ca_submit= Button(creation_window, text="Submit", command= store_variables)
    ca_submit.grid(row=6 ,column=0 ,columnspan=2)

    ca_reset = Button(creation_window, text=' Reset ', command=SetToZero)
    ca_reset.grid(row=6,column=1, columnspan=2)

    
    #executing the window
    creation_window.mainloop()

    
