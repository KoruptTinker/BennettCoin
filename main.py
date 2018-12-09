#importing important modules
import tkinter as tk #imported GUI library
from tkinter import *
from tkinter import messagebox
from create_acc import *
from sign_up import *


#defining the main window
main_window=tk.Tk()
main_window.title("Bennett Coin System")

#functions
def aboutuscallback():  #about us message display
    tk.messagebox.showinfo("About Us", "Created by Brijesh Kumar, Samarth Agarwal, Digvijay Singh, Jai Kumawat, Ansh Grover")

def close(): #function to close a window
    main_window.destroy()


  

#main window

#content of the window
header=Label(main_window, text="Bennett Coin")
header.config(font=("Ariel", 30))
header.grid(row=0)

para=Label(main_window, text="Welcome to Bennett Coin App")
para.config(font=("Ariel", 10))
para.grid(row=1)

option_label=Label(main_window, text="Select an option to proceed further :-")
option_label.grid(row=2, column=0)

option1=Button(main_window, text="New User?", command= ca_window)
option1.grid(row=2, column=1)

option2=Button(main_window, text="Log-In", command=su_window)
option2.grid(row=2, column=2)

about_us=Button(main_window, text="Credits", command= aboutuscallback)
about_us.grid(row=3)

#executing the window
main_window.mainloop()

