from tkinter import *

class converter:
    def __init__(self):

        # init
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        self.temp_frame = Frame()
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, 
                                  text="Temperature Converter",
                                  font=("Arial","16","bold"))

        self.temp_heading.grid(row=0)

        instructions = "Please enter the temperature below..."
        self.temp_instructions = Label(self.temp_frame, text=instructions,wrap=250,width=40,justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Aria", "14"))
        self.temp_entry.grid(row=2,padx=10,pady=10)

        error = "Please enter a number"
        self.temp_error = Label(self.temp_frame, text=error,
                                fg="#9C0000")
        self.temp_error.grid(row=3)

        # button frame
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)
        
        # buttons
        # celsius
        self.to_celsius_button = Button(self.button_frame,
                                         text="To Celsius"
                                         ,bg="#990099",
                                         fg=button_fg,
                                         font=button_font, 
                                         width=12)
        self.to_celsius_button.grid(row=0,column=0,padx=5,pady=5)

        # farehnheit button
        self.to_farenheit_button = Button(self.button_frame,
                                           text="To Farenheit",
                                           bg="#009900",
                                           fg=button_fg,
                                           font=button_font,
                                           width=12)
        self.to_farenheit_button.grid(row=0,column=1,padx=5,pady=5)

        # other buttons
        self.to_help_button = Button(self.button_frame,
                                    text="Help",
                                    bg="#101010",
                                    fg=button_fg,
                                    font=button_font,
                                    width=12)
        self.to_help_button.grid(row=1,column=0,padx=5,pady=5)

        # history
        self.to_history_button = Button(self.button_frame, 
                                        text="History / Export",
                                        bg="#FFA500",fg=button_fg,
                                        font=button_font,width=12,
                                        state=DISABLED)
        self.to_history_button.grid(row=1,column=1,padx=5,pady=5)

        





if __name__ == "__main__":
    root = Tk()
    root.title("temperature converter")
    converter()
    root.mainloop()

