import tkinter as tk
from tkinter import *

import sqlite3
def pn_window():
    #defining window
    paynow_window=tk.Tk()
    paynow_window.title("Pay a person")

    #functions
    def acc_pay():
        uid=pn_entry1.get()
        amount=pn_entry2.get()
        conn=sqlite3.connect('new.db')
        c=conn.cursor()
        c.execute("SELECT * FROM users WHERE Unique_ID = ?",(uid,))
        results=c.fetchall()
        print(results)
    def pay_now():
        uid=pn_entry1.get()
        amount=pn_entry2.get()
        conn=sqlite3.connect('new.db')
        c=conn.cursor()
        c.execute("UPDATE users SET Balance = Balance + ? WHERE Unique_ID = ?",(amount, uid))
        c.execute("SELECT * FROM users WHERE Unique_ID = ?", (uid,))
        conn.commit()
        results = c.fetchall()
        print(results)
    def SetToZero():
        pn_entry1.delete('0', END)
        pn_entry2.delete('0', END)
        
        
        
        
    
    #main body
    pn_header= Label(paynow_window, text="Pay a user")
    pn_header.config(font=("Ariel", 20))
    pn_header.grid(row=0, column=0, columnspan=2)

    pn_option1= Label(paynow_window, text="Enter Unique ID of the user:")
    pn_option1.config(font=("Ariel", 10))
    pn_option1.grid(row=1, column=0)

    pn_entry1= Entry(paynow_window)
    pn_entry1.grid(row=1, column=1)

    pn_option2= Label(paynow_window, text="Enter amount to pay")
    pn_option2.config(font=("Ariel", 10))
    pn_option2.grid(row=2, column=0)

    pn_entry2= Entry(paynow_window)
    pn_entry2.grid(row=2, column=1)

    pn_button= Button(paynow_window, text="Pay", command=pay_now)
    pn_button.grid(row=3, column=0)

    pn_reset=Button(paynow_window, text="Reset", command=SetToZero)
    pn_reset.grid(row=3, column=1)

    #executing the window
    paynow_window.mainloop()
pn_window()
