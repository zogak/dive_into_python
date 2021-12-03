from tkinter import *

win = Tk()
win.geometry("400x300")
win.title("zogak")

ent = Entry()
ent.pack()

def valueSubmit():
    value = ent.get()
    print(value)

btn = Button(win)
btn.config(text = "submit")
btn.config(command = valueSubmit)
btn.pack()

win.mainloop()