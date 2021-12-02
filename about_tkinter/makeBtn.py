from tkinter import *

def btnCommand():
    print("button was clicked")

win = Tk()
win.geometry("100x100")
win.title("zogak")
win.option_add("*Font", "맑은고딕 25")

btn = Button(win)
btn.config(text="click")
btn.config(width=40, height=30)
btn.config(command=btnCommand)
btn.pack()

win.mainloop()