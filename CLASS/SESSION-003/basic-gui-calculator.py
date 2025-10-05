from tkinter import *

window = Tk()
window.title('Basic GUI Calculator')
window.geometry('300x150')

msg1 = Label(window, text='Enter number 1:')
msg1.grid(row=0,column=0)

v1 = IntVar()
e1 = Entry(window, textvar=v1)
e1.grid(row=0, column=1)

msg2 = Label(window, text='Enter number 2 :')
msg2.grid(row=1, column=0)

v2 = IntVar()
e2 = Entry(window, textvar=v2)
e2.grid(row=1, column=1)

op = StringVar()
output = Label(window, text='', textvar=op)
output.grid(row=3, column=0)

def add():
    n1 = v1.get()
    n2 = v2.get()
    s = str(n1+n2)
    op.set('The result of addition is:' + s)

b1 = Button(window, text='Add')
b1.configure(command=add)
b1.grid(row=2, column=0)

def subtract():
    n1 = v1.get()
    n2 = v2.get()
    s = str(n1-n2)
    op.set('The result of substraction is :' + s)

b2 = Button(window, text='Subtract')
b2.configure(command=subtract)
b2.grid(row=2, column=1)

window.mainloop()

