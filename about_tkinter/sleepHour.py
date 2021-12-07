'''
/little_work/sleepHour의 UI를 만든 버전
'''
from tkinter import *
def calculate():
    pass

win = Tk()
win.geometry("600x400")
win.title("Sleeping Hour")
win.option_add("*Font", "맑은고딕 20")

wakeUpLabel = Label(win)
wakeUpLabel.config(text = "일어나는 시간은?")
wakeUpLabel.pack()

wakeHour = Entry(win)
wakeHour.pack()
wakeMinute = Entry(win)
wakeMinute.pack()

sleepLabel = Label(win)
sleepLabel.config(text="자는 시간은?")
sleepLabel.pack()

sleepHour = Entry(win)
sleepHour.pack()
sleepMinute = Entry(win)
sleepMinute.pack()

submitButton = Button(win)
submitButton.config(text="나의 수면 시간은?")
#submitButton.config(width = 40, height= 10)
submitButton.config(command=calculate)
submitButton.pack()

win.mainloop()
