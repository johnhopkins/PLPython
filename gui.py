from tkinter import *
from matchday import *
from tkDatePanel import *
from datetime import *
from match import *
from round import *


class Application(Frame):

    def gotomatchday(self):

        date = datetime(self.datepanel.variable3.get(), self.datepanel.variable2.get(), self.datepanel.variable1.get()).date()
        self.myMatchDay.setDate(date)
        self.label1.grid_forget()
        self.label1 = Label(self.frame1)
        self.label1['text'] = str(self.myMatchDay.date.strftime('%d %B %Y'))
        self.label1.grid(row=3, column=3)
        print(self.myMatchDay.getDate())

    def createwidgets(self):

        self.frame1 = Frame(root)
        self.label = Label(self.frame1)
        self.label['text'] = 'Enter the date the Matches are to be played'
        self.label.grid(row=0, column=0, columnspan=3)
        self.datepanel = DatePanel(self.frame1)
        self.datepanel.grid(row=1, column=0, columnspan=3)
        self.ok = Button(self.frame1, text='Set Date', command=self.gotomatchday)
        self.ok.grid(row=3, column=1)
        self.label1 = Label(self.frame1)
        self.label1['text'] = str(self.myMatchDay.date.strftime('%d %B %Y'))
        self.label1.grid(row=3, column=3)
        self.frame1.grid()
        print(self.round.getnumberofmatchdays())
        print('Round ' + str(self.round.getmatchround()))

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.myMatchDay = MatchDay()
        self.round = Round(11)
        self.grid()
        self.createwidgets()

root = Tk()
app = Application(root)
app.mainloop()