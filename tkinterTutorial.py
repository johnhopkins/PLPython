import tkinter as tk
from tkDatePanel import *
from matchpicker import *
from fixtures import *

root = tk.Tk()

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)



test = DatePanel(frame1).grid()
test2 = MatchPicker(frame2).grid()
test3 = Fixtures(frame3).grid()

frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)
frame3.grid(row=1, column=0, rowspan=10)

root.mainloop()