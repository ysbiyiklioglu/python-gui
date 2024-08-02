import tkinter as tk
import mysql.connector
from tkinter import * 
pencere = tk.Tk()

pencere.geometry("300x600")




connection = mysql.connector.connect(host="localhost",user="root",password="root",port="3306",database="gui")

c=connection.cursor()


c.execute("SELECT * FROM log_in limit 0,10")
i=0 
for log_in in c: 
    for j in range(len(log_in)):
        e = Entry(pencere, width=10, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, log_in[j])
    i=i+1


pencere.mainloop()