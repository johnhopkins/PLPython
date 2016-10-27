from tkinter import *
from matchday import *
from tkDatePanel import *
from datetime import *
from match import *
from round import *


class Application(Frame):

    def addmatchday(self):
        self.mymatchday = MatchDay(datetime(self.datepanel.variable3.get(), self.datepanel.variable2.get(), self.datepanel.variable1.get()).date())
        print(self.mymatchday.getDate())
        self.frame1.grid_forget()

    def createwidgets(self):

        self.frame1 = Frame(root)
        self.label = Label(self.frame1)
        self.label['text'] = 'Enter the date the Matches are to be played'
        self.label.grid(row=0, column=0, columnspan=3)
        self.datepanel = DatePanel(self.frame1)
        self.datepanel.grid(row=1, column=0, columnspan=3)
        self.addmatchdaybutton = Button(self.frame1, text='Add Match Day', command=self.addmatchday)
        self.addmatchdaybutton.grid(row=3, column=2)
        self.label1 = Label(self.frame1)
        self.label1.grid(row=3, column=3)
        self.frame1.grid()

        self.frame2 = Frame(root)
        self.label2 = Label(self.frame2)
        self.label['text'] = 'Pick some fixtures'

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createwidgets()

root = Tk()
app = Application(root)
app.mainloop()