from tkinter import *
from fixtures import *

class MatchPicker(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.teams = ['Crystal Palace','Leicester','Middlesbrough','Bournemouth','Southampton','Sunderland','Stoke','Liverpool','West Brom','Arsenal','Tottenham','West Ham','Watford','Everton','Chelsea','Man United','Man City','Hull City','Burnley','Swansea']
        self.a = 2
        self.teams.sort()
        for team in self.teams:
            self.button = Button(text=team, width=12, command=Fixtures.test)
            self.button.grid(row=self.a, column=1)
            self.a += 1
