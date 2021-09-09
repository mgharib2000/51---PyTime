import tkinter as tk
from tkinter import *
from time import strftime

app = tk.Tk()
app.title("PyClock")
app.iconbitmap("clock.ico")
app.geometry("240x160")
#app.configure(bg="")
app.resizable(False, False)

app.columnconfigure(0, weight=1)

app.rowconfigure(0, weight=1)
app.rowconfigure(1, weight=1)

appFrame = LabelFrame(app, bg = "black", fg = "white", font = ("Latin", 34, "bold"), relief = GROOVE)
appFrame.grid(column=0, row=0, ipadx=5, ipady=10)

def update_label():
    current_time = strftime('%H: %M: %S')
    appFrame.configure(text = current_time)
    appFrame.after(80, update_label)

update_label()
app.mainloop()
