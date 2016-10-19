from tkinter import *

class View(Frame):
    def __init__(self, root):
        self.frame = Frame(self, root)
        self.sidepanel=SidePanel(self.frame)
        self.sidepanel.grid(row=0, column=0)
        self.sidepanel2=SidePanel2(self.frame)
        self.sidepanel2.grid(row=0, column=1)

class SidePanel(Frame):
    def __init__(self, master):
        self.frame = Frame(self, master)
        self.plotBut = Button(self.frame, text="Plot")
        self.plotBut.grid(row=0, column=0)
        self.clearButton = Button(self.frame, text="Clear")
        self.clearButton.grid(row=0, column=1)
        self.cButton = Button(self.frame, text="Spam")
        self.cButton.grid(row=1, column=0)
        self.clButton = Button(self.frame, text="Eggs")
        self.clButton.grid(row=1, column=1)

class SidePanel2(Frame):
    def __init__(self, master):
        self.frame = Frame(self, master)
        self.plotBut = Button(self.frame, text="1")
        self.plotBut.grid(row=0, column=0)
        self.earButton = Button(self.frame, text="2")
        self.earButton.grid(row=0, column=1)
        self.arButton = Button(self.frame, text="3")
        self.arButton.grid(row=1, column=0)
        self.rButton = Button(self.frame, text="4")
        self.rButton.grid(row=1, column=1)

root = Tk()

root.mainloop()