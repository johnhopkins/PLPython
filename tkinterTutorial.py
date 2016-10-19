from tkinter import *
from datetime import *

class ScrolledList( Frame ):
   def __init__( self, parent, **options ):
      Frame.__init__( self, parent, **options )

      self._list = Listbox( self )
      self._scrollbar = Scrollbar( self )

      self._list.pack( side=LEFT )
      self._scrollbar.pack( side=LEFT )

class DatePanel(Frame):
    '''A basic date selector widget that can be used in any tkinter project.
    Requires tkinter (obviously) and datetime modules.'''
    def __init__(self, parent, **options):
        Frame.__init__(self, parent, **options)
        self.dayLabel = Label(self, text="Day")
        self.monthLabel = Label(self, text="Month")
        self.yearLabel = Label(self, text="Year")
        self.dayLabel.grid(row=0, column=0)
        self.monthLabel.grid(row=0, column=1)
        self.yearLabel.grid(row=0, column=2)
        optionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        self.variable1 = IntVar()
        self.variable1.set(datetime.today().day)
        self.dropMenu1 = OptionMenu(self, self.variable1, *optionList)
        self.dropMenu1.grid(row=1, column=0)
        optionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.variable2 = IntVar()
        self.variable2.set(datetime.today().month)
        self.dropMenu2 = OptionMenu(self, self.variable2, *optionList)
        self.dropMenu2.grid(row=1, column=1)
        optionList = [2016, 2017, 2018, 2019, 2020, 2021]
        self.variable3 = IntVar()
        self.variable3.set(datetime.today().year)
        self.dropMenu3 = OptionMenu(self, self.variable3, *optionList)
        self.dropMenu3.grid(row=1, column=2)

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Grid Manager")

        for r in range(6):
            self.master.rowconfigure(r, weight=1)
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            Button(master, text="Button {0}".format(c)).grid(row=6,column=c,sticky=E+W)

        Frame1 = Frame(master, bg="red")
        Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        Button(Frame1, text="Button {0}").grid(row=0,column=1)

        Frame3 = Frame(master, bg="green")
        Frame3.grid(row = 0, column = 2, rowspan = 6, columnspan = 3, sticky = W+E+N+S)

        Button(Frame1, text="Button {0}").grid(row=1,column=0)

        Button(Frame1, text="Button {0}").grid(row=1, column=3)

        DatePanel(Frame3).grid(row=0, column=2)
        DatePanel(Frame1).grid(row=0, column=2)

root = Tk()
root.geometry("400x200+200+200")
app = Application(master=root)
app.mainloop()