from tkinter import *
from tkinter.ttk import *
from math import floor
from TwitterStreamListener import *
from HashtagFilter import *
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

        # generate that many items (this links to Bohdan's code)
        # ds = [["summer", "Damn i miss summer already #japan #summer"],
        #       ["summer", "#summer #2021freeagency is everything"],
        #       ["summer", "Looking to get into shape for #summer - we've got the perfect Apple Watch strap for you! "
        #                  "Check out our #AppleWatch Sport Bands below..."],
        #       ["summer", "Monoprinting - dreaming of #summer #holidays"]]

        ds = TwitterStreamListener.search_tweets(dataset_size, hashtag)

        ds = [(tweet_text, HashtagFilter.filter(hashtag_list)) for tweet_text, hashtag_list in ds]

        for row in ds:
            # write to output file
            # format: ht1,ht2,...; post text
            str = ""

            for ht in row[1]:
                str += ht
                str += ","

            str = str[:-1:]
            out.write(str)
            out.write("; ")

            # write out the post text
            out.write(ascii(row[0]))
            out.write("\n")

        # update progress bar
        # self.prog += num
        self.progress['value'] = (i + 1) * 10

        out.close()

        # when finished with generation, move on
        cmp_lbl = Label(self, text="Dataset generation complete! Output file: " + filename + ".txt", font=LARGE_FONT)
        cmp_lbl.pack(pady=10, padx=10)

        finish_btn = Button(self, text="View Summary",
                            command=lambda: self.controller.feedback(ds))
        finish_btn.pack()
