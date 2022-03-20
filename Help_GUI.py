from tkinter import *
import random


class Convertor:
    def __init__(self):
        print("hello world")

        #Formatting variables
        background_color = "light blue"

        #
        self.converter_frame = Frame (width = 500, height=700,
                                      bg=background_color, pady = 10)
        self.converter_frame.grid()

        #Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text = "Temperature Converter",
                                          font = ("Arial","16","bold"),
                                          bg = background_color,
                                          padx = 10, pady = 10)
        self.temp_converter_label.grid(row=0)

        #Help button (row 1)
        self.help_button = Button(self.converter_frame, text = "Help",
                                  font = ("Arial","14"),
                                  bg = background_color,
                                  padx = 10,pady = 10)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help()
        get_help.help_text.configure(text = "Help text goes here")


        
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor()
    root.mainloop()
