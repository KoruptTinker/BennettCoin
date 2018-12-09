#importing libraries
import tkinter as tk
from tkinter import *

import sqlite3
conn = sqlite3.connect('new.db')
c=conn.cursor()
def my_account():
    myacc_window=tk.Tk()
    myacc_window.title("My Account")

    #functions
    def close_window():
        myacc_window.Destroy()

    def uniqueidcallback():
        conn = sqlite3.connect('new.db')
        c=conn.cursor()
        c.execute("Select Unique_ID from users WHERE Unique_ID=?",(uid,))
        result = c.fetchone()
        tk.messagebox.showinfo("Unique ID", "Your  unique ID  is :-", result)

    #main body
    ma_header= Label(myacc_window, text="Account Summary")
    ma_header.config(font=("Ariel", 20))
    ma_header.grid(row=0, column=0, columnspan=2)

    ma_welcome= Label(myacc_window, text="Welcome,")
    ma_welcome.config(font=("Ariel", 15))
    ma_welcome.grid(row=1, column=0)

    ma_label1 = Label(myacc_window, text="Total Expenditure:")
    ma_label1.config(font=("Ariel",10))
    ma_label1.grid(row=2, column=0)

    ma_label112 = Label(myacc_window, text= "rupees")
    ma_label112.config(font=("Ariel", 10))
    ma_label112.grid(row=2, column=1)
 
    ma_label2 = Label(myacc_window,  text="Current Balance:-")
    ma_label2.config(font=("Ariel", 10))
    ma_label2.grid(row=3,  column=0)

    ma_label22 = Label(myacc_window,  text="rupees")
    ma_label22.config(font=("Ariel", 10))
    ma_label22.grid(row=3, column=1)

    ma_pay = Button(myacc_window, text="Pay Someone")
    ma_pay.grid(row=4, column=0)

    ma_uid = Button(myacc_window, text="View unique ID", command= uniqueidcallback)
    ma_uid.grid(row=4, column=1)

    ma_close = Button(myacc_window, text="Close", command=close_window)
    ma_close.grid(row =4,  column =2)

    
    #executing the window
    myacc_window.mainloop()    
                     


