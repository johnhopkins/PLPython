import tkinter as tk
from startpage import StartPage
from pageone import PageOne
from pagetwo import PageTwo

LARGE_FONT = ("Verdana", 18)

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, controller):

        frame = self.frames[controller]
        frame.tkraise()

        #code to destroy previous frame goes here
        #previous frame destroy

app = Application()
app.mainloop()