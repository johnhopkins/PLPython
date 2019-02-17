import tkinter as tk
import fixtures as fix


class MatchPicker(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.teams = ['Crystal Palace','Leicester','Wolves','Bournemouth','Southampton','Brighton','Fulham','Liverpool','Huddersfield','Arsenal','Tottenham','West Ham','Watford','Everton','Chelsea','Man United','Man City','Newcastle','Burnley','Cardiff']
        self.teams.sort()
        for team in self.teams:
            self.button = tk.Button(text=team, width=12, command=lambda team=team: fix.Fixtures.test(team))
            self.button.pack()
