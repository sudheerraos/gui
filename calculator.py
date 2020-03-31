from tkinter import *

box = Tk()
box.title("My Calculator")

entry = Entry(box, width=40, fg='blue')
entry.grid(row=0, column=0, padx=2, pady=2, columnspan=4)


def bu1click():
    entry.insert(END, '1')


def bu2click():
    entry.insert(END, '2')


def bu3click():
    entry.insert(END, '3')


def bu4click():
    entry.insert(END, '4')


def bu5click():
    entry.insert(END, '5')


def bu6click():
    entry.insert(END, '6')


def bu7click():
    entry.insert(END, '7')


def bu8click():
    entry.insert(END, '8')


def bu9click():
    entry.insert(END, '9')


def bu0click():
    entry.insert(END, '0')


def buaddclick():
    entry.insert(END, '+')


def busubclick():
    entry.insert(END, '-')


def bumulclick():
    entry.insert(END, '*')


def budivclick():
    entry.insert(END, '/')


def buclearclick():
    entry.delete(0, END)


def buequalclick():
    if entry.get() != "":
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)


bu_1 = Button(box, text="1", padx=25, pady=10, command=bu1click)
bu_2 = Button(box, text="2", padx=25, pady=10, command=bu2click)
bu_3 = Button(box, text="3", padx=25, pady=10, command=bu3click)
bu_4 = Button(box, text="4", padx=25, pady=10, command=bu4click)
bu_5 = Button(box, text="5", padx=25, pady=10, command=bu5click)
bu_6 = Button(box, text="6", padx=25, pady=10, command=bu6click)
bu_7 = Button(box, text="7", padx=25, pady=10, command=bu7click)
bu_8 = Button(box, text="8", padx=25, pady=10, command=bu8click)
bu_9 = Button(box, text="9", padx=25, pady=10, command=bu9click)
bu_0 = Button(box, text="0", padx=25, pady=10, command=bu0click)

bu_a = Button(box, text="+", padx=25, pady=10, command=buaddclick)
bu_eq = Button(box, text="=", padx=25, pady=10, command=buequalclick)
bu_cl = Button(box, text="C", padx=25, pady=10, command=buclearclick)

bu_sub = Button(box, text="-", padx=25, pady=10, command=busubclick)
bu_mul = Button(box, text="*", padx=25, pady=10, command=bumulclick)
bu_div = Button(box, text="/", padx=25, pady=10, command=budivclick)

bu_1.grid(row=3, column=0)
bu_2.grid(row=3, column=1)
bu_3.grid(row=3, column=2)
bu_4.grid(row=2, column=0)
bu_5.grid(row=2, column=1)
bu_6.grid(row=2, column=2)
bu_7.grid(row=1, column=0)
bu_8.grid(row=1, column=1)
bu_9.grid(row=1, column=2)
bu_0.grid(row=4, column=0)

bu_mul.grid(row=1, column=3)
bu_div.grid(row=2, column=3)

bu_sub.grid(row=3, column=3)
bu_a.grid(row=4, column=3)

bu_eq.grid(row=4, column=2)
bu_cl.grid(row=4, column=1)

box.mainloop()
