from Tkinter import *
from ttk import *
import time

LARGE_FONT = ("Verdana", 12)
hashtag = ""
dataset_size = 0

class WebData(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, GenerateDataset, CompletedDataset):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        ht_entry_lbl = Label(self, text="Welcome to Web Data! Please enter 1 or more hashtags (separated by spaces). \n"
                                        "Example: 'day bird tree summer'", font=LARGE_FONT)
        ht_entry_lbl.pack(pady=10, padx=10)

        ht_ent = Entry(self)
        ht_ent.pack()

        reg = Frame.register(self, ht_callback)
        ht_ent.config(validate="key", validatecommand=(reg, '%P'))

        num_entry_lbl = Label(self, text="Please enter the number of tweets you would like to retrieve for the dataset:",
                      font=LARGE_FONT)
        num_entry_lbl.pack(pady=10, padx=10)

        num_ent = Entry(self)
        num_ent.pack()

        reg = Frame.register(self, num_callback)
        num_ent.config(validate="key", validatecommand=(reg, '%P'))

        generate_button = Button(self, text="Generate Dataset",
                                 command=lambda: start_generate(ht_ent.get(), num_ent.get(), controller))
        generate_button.pack()


def num_callback(input):
    return input.isdigit()

def ht_callback(input):
    # note: if the user types multiple consecutive spaces this won't catch that
    temp = input.replace(" ", "")
    return temp.isalnum()

# start dataset generation
def start_generate(ht, size, controller):
    hastag = ht #TODO eventually change this to parse a list of hashtags
    dataset_size = size
    controller.show_frame(GenerateDataset)

class GenerateDataset(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lbl = Label(self, text="Generating Dataset...", font=LARGE_FONT)
        lbl.pack(pady=10, padx=10)

        progress = Progressbar(self, orient=HORIZONTAL, length=100, mode='determinate')
        progress.pack()

        back_btn = Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        back_btn.pack()

    def generate(self):
        # TODO replace this code with stuff to actually generate dataset (and update progress bar)
        for i in range(10):
            # find out how many things to generate
            num = dataset_size / 10
            # add 1 if needed to take care of the remainder
            if i < dataset_size % 10:
                num += 1

            # generate that many items (this links to Bohdan's code)
            # TODO write this
            #time.sleep(1)

            # write items to output file
            # TODO write this (if Bohdan doesn't do it)

            # update progress bar
            #progress['value'] = (i + 1) * 10

        # when finished with generation, move on
        # controller.show_frame(CompletedDataset)

        cmp_lbl = Label(self, text="Dataset generation complete! Output file: output.txt", font=LARGE_FONT)
        cmp_lbl.pack(pady=10, padx=10)

        finish_btn = Button(self, text="View Summary",
                            command=lambda: controller.show_frame(CompletedDataset))
        finish_btn.pack()


class CompletedDataset(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Dataset Generation Complete!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        sample_data = Label(self, text="Here is a sample Twitter post!", font=LARGE_FONT)
        sample_data.pack()

        lbl_hashtags = Label(self, text="Relevant Hashtags: Dog, Pet, Cute")
        lbl_hashtags.pack()

        button1 = Button(self, text="Generate Another Dataset",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = Button(self, text="Export",
                            command=lambda: controller.show_frame(CompletedDataset))
        button2.pack()


app = WebData()
app.mainloop()
