from tkinter import *
import calendar

root = Tk()
root.title("Calendar")
root.geometry("600x800")
year = 2020
mycal = calendar.calendar(year)
cal_year = Label(root , text = mycal , font = "Algerian,10,bold").pack()
root.mainloop()