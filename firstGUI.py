# GUI program to store users and passwords and display them on the terminal

from tkinter import *
from tkinter import messagebox

box = Tk()
box.title('GUI Exercise')

label_head = Label(box, text = 'GUI program to store User and Passwords and Show them')
label_head.grid(row=0, column=0, columnspan = 2)

label1 = Label(box, text = 'Name : ', bg='blue', fg='white', width=8, anchor='w')
label1.grid(row = 1, column = 0, columnspan = 1)

entry1 = Entry(box,width = 50)
entry1.grid(row = 1, column = 1, columnspan =1)

label2 = Label(box, text = 'Password : ', bg='blue', fg='white', width=8)
label2.grid(row = 2, column = 0, columnspan = 1)

entry2 = Entry(box,width = 50)
entry2.grid(row = 2, column = 1, columnspan =1)

button1 = Button(box, text = 'Submit', bg = 'brown', fg = 'white')
button1.grid(row = 3, column = 0)

button2 = Button(box, text = 'Show', bg = 'brown', fg = 'white')
button2.grid(row = 3, column = 1)

user_name = []
user_pwd = []


def button1_click():
    if entry1.get() == "" or entry2.get() == "":
        messagebox.showwarning(title="Warning!", message="Name or Password Cannot be blank. Please enter a value")
        entry1.delete(0, 'end')
        entry2.delete(0, 'end')
    else:
        user_name.append(entry1.get())
        user_pwd.append(entry2.get())

    entry1.delete(0,'end')
    entry2.delete(0, 'end')


def button2_click():
    print(f"User names are: {user_name}")
    print(f"Passwords are: {user_pwd}")


button1.configure(command=button1_click)
button2.configure(command=button2_click)


box.mainloop()
