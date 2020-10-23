from tkinter import *
from tkinter.ttk import *
import time
from CompletedDatasetPage import *
from GenerateDatasetPage import *
from StartPage import *

LARGE_FONT = ("Verdana", 12)


class WebData(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, GenerateDatasetPage, CompletedDatasetPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # def show_frame(self, cont):
    #     frame = self.frames[cont]
    #     frame.tkraise()

    def restart(self):
        frame = self.frames[StartPage]
        frame.tkraise()

    def generate(self):
        frame = self.frames[GenerateDatasetPage]
        frame.tkraise()

    def feedback(self):
        frame = self.frames[CompletedDatasetPage]
        frame.tkraise()

app = WebData()
app.mainloop()
