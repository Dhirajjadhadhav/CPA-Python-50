from tkinter import *

root_window = Tk()
root_window.geometry('300x200')
root_window.title('My First Window')

msg  = Label(root_window, text='PY50124_dhiraj_jadhav')
msg.grid(row=0, column=0)

root_window.mainloop()