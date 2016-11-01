import tkinter as tk

LARGE_FONT = ("Verdana", 18)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        from startpage import StartPage
        from pagetwo import PageTwo
        from matchpicker import MatchPicker

        label = tk.Label(self, text="Match Picker", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two", command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        mymatchpicker = MatchPicker(self)
        mymatchpicker.pack()