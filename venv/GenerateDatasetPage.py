from Tkinter import *
from ttk import *
import time
from CompletedDatasetPage import *

LARGE_FONT = ("Verdana", 12)

class GenerateDatasetPage(Frame):

    def __init__(self, parent, cont):
        self.prog = 0
        self.controller = cont

        Frame.__init__(self, parent)
        lbl = Label(self, text="Generating Dataset...", font=LARGE_FONT)
        lbl.pack(pady=10, padx=10)

        self.progress = Progressbar(self, orient=HORIZONTAL, length=100, mode='determinate', variable=self.prog)
        self.progress.pack()

        back_btn = Button(self, text="Back to Home", command=lambda: self.controller.show_frame(StartPage))
        back_btn.pack()

    def generate(self, dataset_size, hashtag, filename):
        # TODO replace this code with stuff to actually generate dataset (and update progress bar)
        for i in range(10):
            # find out how many things to generate
            num = dataset_size / 10
            # add 1 if needed to take care of the remainder
            if i < dataset_size % 10:
                num += 1
            print(num)

            # generate that many items (this links to Bohdan's code)
            # TODO write this
            time.sleep(1)

            # write items to output file
            # TODO write this (if Bohdan doesn't do it)

            # update progress bar
            #self.prog += num
            self.progress['value'] = (i + 1) * 10

        # when finished with generation, move on
        cmp_lbl = Label(self, text="Dataset generation complete! Output file: " + filename, font=LARGE_FONT)
        cmp_lbl.pack(pady=10, padx=10)

        finish_btn = Button(self, text="View Summary",
                            command=lambda: self.controller.show_frame(CompletedDatasetPage))
        finish_btn.pack()
