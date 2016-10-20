from tkDatePanel import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title("Grid Manager")

        for r in range(6):
            self.master.rowconfigure(r, weight=2)
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            Button(master, text="Button {0}".format(c)).grid(row=6,column=c,sticky=E+W)

        Frame1 = Frame(master, bg="red")
        Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        Frame2 = Frame(master, bg="blue")
        Frame2.grid(row = 3, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        Frame3 = Frame(master, bg="green")
        Frame3.grid(row = 0, column = 2, rowspan = 6, columnspan = 3, sticky = W+E+N+S)

        Button(Frame3, text="Button A").grid(row=0, column=0)
        Button(Frame3, text="Button B").grid(row=1, column=0)
        Button(Frame3, text="Button C").grid(row=2, column=0)

        DatePanel(Frame1).grid(row=0, column=2, rowspan=2)

        Button(Frame2, text="Button X").grid(row=0, column=0)
        Button(Frame2, text="Button Y").grid(row=0, column=1)
        Button(Frame2, text="Button Z").grid(row=0, column=2)


root = Tk()
root.geometry("600x300")
app = Application(master=root)
app.mainloop()