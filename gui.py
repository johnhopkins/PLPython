from tkinter import *
from matchday import *
from datetime import *

class Application(Frame):

    def setTheMatchdayDate(self):
        self.myMatchDay.setDate(datetime((self.variable3.get()), (self.variable2.get()), (self.variable1.get())).date())
        print(self.myMatchDay.date)

    def createWidgets(self):

        self.day = Label(self.master)
        self.day['text'] = 'Day'
        self.day.grid(row=1, column=1, sticky='W', )

        optionList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        self.variable1 = IntVar()
        self.variable1.set(datetime.today().day)
        self.dropMenu1 = OptionMenu(self.master, self.variable1, *optionList)
        self.dropMenu1.grid(row=2, column=1, sticky='W')

        self.month = Label(self.master)
        self.month['text'] = 'Month'
        self.month.grid(row=1, column=2)

        optionList = [1,2,3,4,5,6,7,8,9,10,11,12]
        self.variable2 = IntVar()
        self.variable2.set(datetime.today().month)
        self.dropMenu2 = OptionMenu(self.master, self.variable2, *optionList)
        self.dropMenu2.grid(row=2, column=2)

        self.year = Label(self.master)
        self.year['text'] = 'Year'
        self.year.grid(row=1, column=3)

        optionList = [2016, 2017, 2018, 2019, 2020, 2021]
        self.variable3 = IntVar()
        self.variable3.set(datetime.today().year)
        self.dropMenu3 = OptionMenu(self.master, self.variable3, *optionList)
        self.dropMenu3.grid(row=2, column=3)

        self.ok = Button(self.master, text='Add Date', command=self.setTheMatchdayDate)
        self.ok.grid(row=3, column=2)

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.variable1 = 0
        self.variable2 = 0
        self.variable3 = 0
        self.createWidgets()
        self.grid()
        self.myMatchDay = MatchDay()

root = Tk()
app = Application(master=root)
app.mainloop()