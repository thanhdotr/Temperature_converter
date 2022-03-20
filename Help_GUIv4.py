from tkinter import *
import random


class Convertor:
    def __init__(self):
        print("hello world")

        # Formatting variables
        background_color = "light blue"

        #
        self.converter_frame = Frame(width=300, height=300,
                                     bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Help button (row 1)
        self.help_button = Button(self.converter_frame, text="Help",
                                  font=("Arial", "14"),
                                  bg=background_color,
                                  padx=10, pady=10)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help()
        get_help.help_text.configure(text="Help text goes here")


class Help:
    def __init__(self):
        background = "orange"

        #disable help button


        # sets up child window (ie:help box)
        self.help_box = Toplevel()
        # set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # set up Help heading(row 0)
        self.how_heading = Label(self.help_frame, text=" Help/Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)
        # Help text( label, row 1)
        self.help_text = Label(self.help_frame, text="", justify=LEFT,
                               width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_tbh = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                                  command=self.close_help)
        self.dismiss_tbh.grid(row=2, pady=10)

    def close_help(self):
        self.help_box.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor()
    root.mainloop()
