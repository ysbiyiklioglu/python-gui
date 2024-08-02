
import tkinter as tk
import mysql.connector
pencere = tk.Tk()


# setting the windows size
pencere.geometry("300x100")

connection = mysql.connector.connect(host="localhost",user="root",password="root",port="3306",database="gui")

c=connection.cursor()

# for storing name and password
name_var = tk.StringVar()
passw_var = tk.StringVar()


# defining a function that will
# get the name and password and
# print them on the screen
def submit():
    name = name_var.get()
    password = passw_var.get()

    print("The name is : " + name)
    print("The password is : " + password)

    name_var.set("")
    passw_var.set("")


# creating a label for
# name using widget Label
name_label = tk.Label(pencere, text='Username', font=('calibre', 10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(pencere, textvariable=name_var, font=('calibre', 10, 'normal'))

# creating a label for password
passw_label = tk.Label(pencere, text='Password', font=('calibre', 10, 'bold'))

# creating a entry for password
passw_entry = tk.Entry(pencere, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')

def insertData():
    firstname = name_entry.get()
    lastname = passw_entry.get()
    insert_query = "INSERT INTO `log_in`(`username`, `password`) VALUES (%s,%s)"
    vals = (firstname,lastname,)
    c.execute(insert_query,vals)
    connection.commit()

sub_btn = tk.Button(pencere, text='Submit', command=insertData)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

pencere.mainloop() 

