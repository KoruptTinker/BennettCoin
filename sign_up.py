import tkinter as tk
from tkinter import *
from tkinter.messagebox import showerror, showinfo
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect('new.db')
c=conn.cursor()

def su_window():
    #creating window
    signin_window=tk.Tk()
    signin_window.title("Log-in")

    #functions
    def verify_cred():
        user=su_entry1.get()
        password=su_entry2.get()    
        c.execute('SELECT * FROM users WHERE Username = ? and Password = ?',(user,password))
        results = c.fetchall()
        print(results)
        if (user=="" or password==""):
            showerror(title = "Error", message = "Fields cannot be blank")
        elif results ==[]:
            showerror(title = "Error", message = "User does not exist")
        elif results:
            for i in results:
                global uid
                uid = i[0]
                global uname
                uname = i[1]
                global pswd 
                pswd = i[2]
                global fname
                fname = i[3]
                global enroll
                enroll = i[4]
                global course
                course = i[5]
                global face
                face = i[6]
                global balance
                balance = i[7]
                global tot_exp
                tot_exp = i[8]
                messagebox.showinfo("Alert", "Welcome " + fname)
                
                
    def SetToZero():
        su_entry1.delete('0', END)
        su_entry2.delete('0', END)
        
            
        
    
    #main body
    su_header= Label(signin_window, text="Log-in")
    su_header.config(font=("Ariel", 20))
    su_header.grid(row=0, column=0, columnspan=2)

    su_option1= Label(signin_window, text="Username")
    su_option1.config(font=("Ariel", 10))
    su_option1.grid(row=1, column=0)

    su_entry1= Entry(signin_window)
    su_entry1.grid(row=1, column=1)

    su_option2= Label(signin_window, text="Password")
    su_option2.config(font=("Ariel", 10))
    su_option2.grid(row=2, column=0)

    su_entry2= Entry(signin_window, show="*")
    su_entry2.grid(row=2, column=1)

    su_login = Button(signin_window, text="Log-in", command= verify_cred)
    su_login.grid(row=3, column=0, columnspan=1)

    su_reset = Button(signin_window, text=' Reset ', command=SetToZero)
    su_reset.grid(row=3,column=1, columnspan=1)
    
    #executing the window
    signin_window.mainloop()
