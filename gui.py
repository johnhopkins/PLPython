from tkinter import *
from matchday import *
from tkDatePanel import *
from datetime import *


class Application(Frame):

    def gotomatchday(self):

        date = datetime(self.variable3.get(), self.variable2.get(), self.variable1.get()).date()
        self.myMatchDay.setDate(date)
        self.label.grid_forget()
        self.label = Label(self.master)
        self.label['text'] = str(self.myMatchDay.date.strftime('%d %B %Y'))
        self.label.grid(row=4, column=2)

    def createwidgets(self):

        self.label = Label(self.master)
        self.label['text'] = 'Enter the date the Matches are to be played'
        self.label.grid(row=0, column=1, columnspan=3)
        self.datepanel = DatePanel(self).grid()
        self.ok = Button(self.master, text='Add Date', command=self.gotomatchday)
        self.ok.grid(row=3, column=2)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.myMatchDay = MatchDay()
        self.grid()
        self.variable1 = None
        self.variable2 = None
        self.variable3 = None
        self.createwidgets()

root = Tk()
app = Application(root)
app.mainloop()