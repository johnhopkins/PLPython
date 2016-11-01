import tkinter as tk

LARGE_FONT = ("Verdana", 18)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        from startpage import StartPage
        from pageone import PageOne
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One", command=lambda: controller.show_frame(PageOne))
        button2.pack()