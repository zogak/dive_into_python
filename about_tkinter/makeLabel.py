from tkinter import *

def clear(event):
    if idEntry.get() == "hello@gmail.com":
        idEntry.delete(0, len(idEntry.get()))

def login():
    idFromRequest = idEntry.get()
    pwFromRequest = pwEntry.get()
    print(idFromRequest)

win = Tk()
win.title("Log-In")
win.geometry("400x300")
win.option_add("*Font", "맑은고딕 20")

# id label
idLabel = Label(win)
idLabel.config(text = "ID")
idLabel.pack()

# id entry
idEntry = Entry(win)
idEntry.insert(0, "hello@gmail.com")
idEntry.bind("<Button-1>", clear)
idEntry.pack()

# pw label
pwLabel = Label(win)
pwLabel.config(text="PW")
pwLabel.pack()

# pw entry
pwEntry = Entry(win)
pwEntry.config(show="●")
pwEntry.pack()

# log-in button
btn = Button(win)
btn.config(text="LOG-IN")
btn.config(command = login)
btn.pack()

win.mainloop()