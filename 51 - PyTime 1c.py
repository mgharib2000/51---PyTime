  
import tkinter as tk
from tkinter import *
from time import strftime

app = Tk()
app.title("PyClock")
app.iconbitmap("clock.ico")
app.geometry("240x80")
app.configure(bg="PURPLE")
app.resizable(False, False)

app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.columnconfigure(2, weight=1)

app.rowconfigure(0, weight=1)
app.rowconfigure(1, weight=1)
app.rowconfigure(2, weight=1)

clock_label = Label(app, bg="black", fg="white", font = ("Times", 40, "bold"), relief=GROOVE)
clock_label.grid(row=1, column=1)

def update_label():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_label)

update_label()
app.mainloop()
