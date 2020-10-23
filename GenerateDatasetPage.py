from tkinter import *
from tkinter.ttk import *
# from CompletedDatasetPage import CompletedDatasetPage
from math import floor
import time

consumerKey = 'jzbDBNIjFjdd6WGuDVqnOzJga'
consumerSecret = 'xea1fCuSMYOXEk96MhFMU3aDac8rkJETBbOtk4tCU8QwHwPRnB'
accessToken = '1246952734185656323-OToMkUAzLLCz1rAjzQth6kJP9k5guY'
accessTokenSecret = '8s65E6nGAB4GHVeEZT7YmRgdQUYpPTtXA7FLXUpcNrQQX'

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

        back_btn = Button(self, text="Back to Home", command=lambda: self.controller.restart())
        back_btn.pack()

    def generate(self, dataset_size, hashtag, filename):
        # open a file to overwrite
        out = open(filename + ".txt", "w")

        # TODO replace this code with stuff to actually generate dataset (and update progress bar)
        for i in range(10):
            # find out how many things to generate
            num = floor(dataset_size / 10)
            # add 1 if needed to take care of the remainder
            if i < dataset_size % 10:
                num += 1
            print(num)

        # generate that many items (this links to Bohdan's code)
        # TODO write this
        #time.sleep(1)
        ds = [["summer", "Damn i miss summer already #japan #summer"],
              ["summer", "#summer #2021freeagency is everything"],
              ["summer", "Looking to get into shape for #summer - we've got the perfect Apple Watch strap for you! "
                         "Check out our #AppleWatch Sport Bands below..."],
              ["summer", "Monoprinting - dreaming of #summer #holidays"]]

        for row in ds:
            # write to output file
            # format: ht1,ht2,...; post text
            for k in range(len(row)-2):
                out.write(row[k])
                out.write(",")
            out.write(row[len(row)-2])
            out.write("; ")
            out.write(row[len(row)-1])
            out.write("\n")

        # update progress bar
        # self.prog += num
        self.progress['value'] = (i + 1) * 10

        out.close()

        # when finished with generation, move on
        cmp_lbl = Label(self, text="Dataset generation complete! Output file: " + filename + ".txt", font=LARGE_FONT)
        cmp_lbl.pack(pady=10, padx=10)

        finish_btn = Button(self, text="View Summary",
                            command=lambda: self.controller.feedback())
        finish_btn.pack()


# class CompletedDatasetPage(Frame):
#
#     def __init__(self, parent, controller):
#         Frame.__init__(self, parent)
#         label = Label(self, text="Dataset Generation Complete!", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         # TODO change this to display actual Twitter data
#         sample_data = Label(self, text="Monoprinting - dreaming of #summer #holidays", font=LARGE_FONT)
#         sample_data.pack()
#
#         lbl_hashtags = Label(self, text="Relevant Hashtags: Summer, Holidays")
#         lbl_hashtags.pack()
#
#         #generate_new_dataset_btn = Button(self, text="Generate Another Dataset",
#         #                    command=lambda: controller.show_frame(StartPage))
#         #generate_new_dataset_btn.pack()

