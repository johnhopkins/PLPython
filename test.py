import tkinter as Tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from datetime import *

class Model():
 
    def __init__(self):
        self.xpoint=200
        self.ypoint=200
        self.res = None

    def calculate(self):
        x,y=np.meshgrid(np.linspace(-5,5,self.xpoint),np.linspace(-5,5,self.ypoint))
        z=np.cos(x**2*y**3) 
        self.res = {"x":x,"y":y,"z":z}
 
class View():
    def __init__(self, master):
        self.frame = Tk.Frame(master)

        # self.fig = Figure( figsize=(7.5, 4), dpi=80 )
        # self.ax0 = self.fig.add_axes( (0.05, .05, .90, .90), axisbg=(.75,.75,.75), frameon=False)

        # self.frame.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        # self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        # self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        # self.canvas.show()

        self.sidepanel=SidePanel(master)
        self.sidepanel.grid(row=0, column=0)
        self.datepanel=DatePanel(master)


class SidePanel():
    def __init__(self, root):
        self.frame = Tk.Frame(root)
        self.frame.pack(side=Tk.RIGHT, fill=Tk.BOTH, expand=1)
        self.plotBut = Tk.Button(self.frame, text="Plot")
        self.plotBut.grid(row=0, column=0)
        self.clearButton = Tk.Button(self.frame, text="Clear")
        self.clearButton.grid(row=0, column=1)

class DatePanel():
    def __init__(self, root):
        self.frame = Tk.Frame(root)
        self.dayLabel = Tk.Label(self.frame, text="Day")
        self.monthLabel = Tk.Label(self.frame, text="Month")
        self.yearLabel = Tk.Label(self.frame, text="Year")
        self.dayLabel.grid(row=0, column=0)
        self.monthLabel.grid(row=0, column=1)
        self.yearLabel.grid(row=0, column=2)
        optionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        self.variable1 = Tk.IntVar()
        self.variable1.set(datetime.today().day)
        self.dropMenu1 = Tk.OptionMenu(self.frame, self.variable1, *optionList)
        self.dropMenu1.grid(row=1, column=0)
        optionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.variable2 = Tk.IntVar()
        self.variable2.set(datetime.today().month)
        self.dropMenu2 = Tk.OptionMenu(self.frame, self.variable2, *optionList)
        self.dropMenu2.grid(row=1, column=1)
        optionList = [2016, 2017, 2018, 2019, 2020, 2021]
        self.variable3 = Tk.IntVar()
        self.variable3.set(datetime.today().year)
        self.dropMenu3 = Tk.OptionMenu(self.frame, self.variable3, *optionList)
        self.dropMenu3.grid(row=1, column=2)

class Controller():
    def __init__(self):
        self.root = Tk.Tk()
        self.model=Model()
        self.view=View(self.root)
        # self.view.sidepanel.plotBut.bind("<Button>",self.my_plot)
        # self.view.sidepanel.clearButton.bind("<Button>",self.clear)
  
    def run(self):
        self.root.title("Tkinter MVC example")
        self.root.mainloop()
         
    def clear(self,event):
        self.view.ax0.clear()
        self.view.fig.canvas.draw()
  
    def my_plot(self,event):
        self.model.calculate()
        self.view.ax0.clear()
        self.view.ax0.contourf(self.model.res["x"],self.model.res["y"],self.model.res["z"])
        self.view.fig.canvas.draw()

if __name__ == '__main__':
    c = Controller()
    c.run()