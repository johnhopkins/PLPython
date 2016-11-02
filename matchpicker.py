import tkinter as tk
from fixtures import *


class MatchPicker(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.teams = ['Crystal Palace','Leicester','Middlesbrough','Bournemouth','Southampton','Sunderland','Stoke','Liverpool','West Brom','Arsenal','Tottenham','West Ham','Watford','Everton','Chelsea','Man United','Man City','Hull City','Burnley','Swansea']
        self.teams.sort()
        for team in self.teams:
            self.button = Button(text=team, width=12, command=lambda: Fixtures.test(self.teams))
            self.button.pack()
