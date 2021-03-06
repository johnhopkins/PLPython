import tkinter as tk
from datetime import *

class DatePanel(tk.Frame):
    '''A basic date selector widget that can be used in any tkinter project.
    Requires tkinter (obviously) and datetime modules.'''
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.dayLabel = tk.Label(self, text="Day")
        self.monthLabel = tk.Label(self, text="Month")
        self.yearLabel = tk.Label(self, text="Year")
        self.dayLabel.grid(row=0, column=0, sticky='ew')
        self.monthLabel.grid(row=0, column=1, sticky='ew')
        self.yearLabel.grid(row=0, column=2, sticky='ew')

        optionlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        self.variable1 = tk.IntVar()
        self.variable1.set(datetime.today().day)
        self.dropMenu1 = tk.OptionMenu(self, self.variable1, *optionlist)
        self.dropMenu1.grid(row=1, column=0)

        optionlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.variable2 = tk.IntVar()
        self.variable2.set(datetime.today().month)
        self.dropMenu2 = tk.OptionMenu(self, self.variable2, *optionlist)
        self.dropMenu2.grid(row=1, column=1)

        optionlist = [2016, 2017, 2018, 2019, 2020, 2021]
        self.variable3 = tk.IntVar()
        self.variable3.set(datetime.today().year)
        self.dropMenu3 = tk.OptionMenu(self, self.variable3, *optionlist)
        self.dropMenu3.grid(row=1, column=2)
