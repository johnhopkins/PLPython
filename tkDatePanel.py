from tkinter import *
from datetime import *


class DatePanel(Frame):
    '''A basic date selector widget that can be used in any tkinter project.
    Requires tkinter (obviously) and datetime modules. Passes the individual
    date (day, month year) variables back to the parent class so that you do
    not need to keep a reference to a DatePanel instance'''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.dayLabel = Label(self, text="Day")
        self.monthLabel = Label(self, text="Month")
        self.yearLabel = Label(self, text="Year")
        self.dayLabel.grid(row=0, column=0, sticky=E+W)
        self.monthLabel.grid(row=0, column=1, sticky=E+W)
        self.yearLabel.grid(row=0, column=2, sticky=E+W)

        optionlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        parent.variable1 = IntVar()
        parent.variable1.set(datetime.today().day)
        self.dropMenu1 = OptionMenu(self, parent.variable1, *optionlist)
        self.dropMenu1.grid(row=1, column=0)

        optionlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        parent.variable2 = IntVar()
        parent.variable2.set(datetime.today().month)
        self.dropMenu2 = OptionMenu(self, parent.variable2, *optionlist)
        self.dropMenu2.grid(row=1, column=1)

        optionlist = [2016, 2017, 2018, 2019, 2020, 2021]
        parent.variable3 = IntVar()
        parent.variable3.set(datetime.today().year)
        self.dropMenu3 = OptionMenu(self, parent.variable3, *optionlist)
        self.dropMenu3.grid(row=1, column=2)