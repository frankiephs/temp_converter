from tkinter import *

class converter:
    def __init__(self):
        self.temp_frame = Frame()
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, 
                                  text="Temperature Converter",
                                  font=("Arial","16","bold"))

        self.temp_heading.grid(row=0)

        instructions = "Please enter the temperature below..."
        self.temp_instructions = Label(self.temp_frame, text=instructions,wrap=250,width=40,justify="left")
        self.temp_instructions.grid(row=1)





if __name__ == "__main__":
    root = Tk()
    root.title("temperature converter")
    converter()
    root.mainloop()

