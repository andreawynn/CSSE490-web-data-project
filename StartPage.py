from tkinter import *
from tkinter.ttk import *
import time
from GenerateDatasetPage import *

LARGE_FONT = ("Verdana", 12)


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        ht_entry_lbl = Label(self, text="Welcome to Web Data! Please enter 1 or more hashtags (separated by spaces). \n"
                                        "Example: 'day bird tree summer'", font=LARGE_FONT)
        ht_entry_lbl.pack(pady=10, padx=10)

        ht_ent = Entry(self)
        ht_ent.pack()

        reg = Frame.register(self, self.ht_callback)
        ht_ent.config(validate="key", validatecommand=(reg, '%P'))

        num_entry_lbl = Label(self, text="Please enter the number of tweets you would like to retrieve for the dataset:",
                      font=LARGE_FONT)
        num_entry_lbl.pack(pady=10, padx=10)

        num_ent = Entry(self)
        num_ent.pack()

        reg = Frame.register(self, self.num_callback)
        num_ent.config(validate="key", validatecommand=(reg, '%P'))

        filename_entry_lbl = Label(self,
                              text="Please enter the full name of the output file for the dataset:",
                              font=LARGE_FONT)
        filename_entry_lbl.pack(pady=10, padx=10)

        fn_ent = Entry(self)
        fn_ent.pack()

        reg = Frame.register(self, self.fn_callback)
        fn_ent.config(validate="key", validatecommand=(reg, '%P'))

        generate_button = Button(self, text="Generate Dataset",
                                 command=lambda: self.start_generate(ht_ent.get(), num_ent.get(), fn_ent.get(), controller))
        generate_button.pack(pady=20, padx=10)

    def num_callback(self, input):
        return input.isdigit() or input == ""

    def fn_callback(self, input):
        return input.isalnum() or input == ""

    def ht_callback(self, input):
        # note: if the user types multiple consecutive spaces this won't catch that
        temp = input.replace(" ", "")
        return temp.isalnum() or input == ""

    # start dataset generation
    def start_generate(self, ht, size, fn, controller):
        #TODO eventually parse a list of hashtags
        controller.show_frame(GenerateDatasetPage) # TODO make this show up before calling generate!
        controller.frames[GenerateDatasetPage].generate(int(size), ht, fn)
