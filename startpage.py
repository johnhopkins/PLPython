import tkinter as tk

LARGE_FONT = ("Verdana", 18)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        from pageone import PageOne
        from pagetwo import PageTwo
        from tkDatePanel import DatePanel

        label = tk.Label(self, text="Enter the date that the matches are to be played", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        datepanel = DatePanel(self)
        datepanel.pack()

        button = tk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Visit Page 2", command=lambda: controller.show_frame(PageTwo))
        button2.pack()

