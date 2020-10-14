from Tkinter import *
from ttk import *
import time
from StartPage import *

LARGE_FONT = ("Verdana", 12)

class CompletedDatasetPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Dataset Generation Complete!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # TODO change this to display actual Twitter data
        sample_data = Label(self, text="Here is a sample Twitter post!", font=LARGE_FONT)
        sample_data.pack()

        lbl_hashtags = Label(self, text="Relevant Hashtags: Dog, Pet, Cute")
        lbl_hashtags.pack()

        generate_new_dataset_btn = Button(self, text="Generate Another Dataset",
                            command=lambda: controller.show_frame(StartPage))
        generate_new_dataset_btn.pack()
