
from tkinter import *
import calendar

def ShowCalender():
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calendar of the year")
    gui.geometry("500x600")
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    CalYear = Label(gui, text=gui_content, font="Consolas 10 bold")
    CalYear.grid(row=5, column=1)
    gui.mainloop()

new = Tk()
new.config(background='grey')
new.title("Calendar")
new.geometry("250x140")
cal = Label(new, text="Calendar", bg='grey', font=("times", 28, "bold"))
year = Label(new, text="Enter year", bg='dark grey')
year_field = Entry(new)
button = Button(new, text='Show Calendar', fg='Black', bg='Blue', command=ShowCalender)

cal.grid(row=1, column=1)
year.grid(row=2, column=1)
year_field.grid(row=3, column=1)
button.grid(row=4, column=1)

new.mainloop()
