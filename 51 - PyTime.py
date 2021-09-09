from time import strftime
from tkinter import Label, Tk

#======= Configuring window =========
app = Tk()
app.title("PyClock")
app.geometry("200x80")
app.configure(bg="grey")
app.resizable(False, False)

app.columnconfigure(0, weight=1)
app.rowconfigure(1, weight=1)

clock_label = Label(app, bg="black", fg="white", font = ("Times", 24, 'bold'), relief='flat')
clock_label.grid(row=1, column=0)

def update_label():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_label)

update_label()
app.mainloop()
