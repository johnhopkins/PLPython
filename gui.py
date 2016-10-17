from tkinter import *
from matchday import *
import datetime

myMatchday = MatchDay()

win = Tk()

win.title('PL Routing')

label = Label(text = 'Input the date')
day = Label(text = 'Day')

variable1 = StringVar(win)
variable1.set(1)
variable2 = StringVar(win)
variable2.set(1)
variable3 = StringVar(win)
variable3.set(2016)

selectedDay = OptionMenu(win, variable1, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
month = Label(text ='Month')
selectedMonth = OptionMenu(win, variable2, 1,2,3,4,5,6,7,8,9,10,11,12)
year = Label(text = 'Year')
selectedYear = OptionMenu(win, variable3, 2016,2017,2018,2019,2020,2021)

label.grid(row = 0, column = 0)
day.grid(row = 1, column = 0)
month.grid(row = 1, column = 2)
year.grid(row = 1, column = 4)
selectedDay.grid(row=1, column = 1)
selectedMonth.grid(row=1, column = 3)
selectedYear.grid(row=1, column = 5)

def ok():

    mydate = datetime.date(int(variable3.get()), int(variable2.get()), int(variable1.get()))
    myMatchday.setDate(mydate)
    print(mydate)

button = Button(win, text="OK", command=ok)
button.grid(row = 2, column = 3)

win.mainloop()