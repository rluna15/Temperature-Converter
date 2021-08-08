

import tkinter
import tkinter.messagebox


class TempCalculation:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create two frames to grounp widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.mid_frame2 = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.quit_frame = tkinter.Frame(self.main_window)

        # Create the widgets for the top frame.
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text='Enter degrees:')
        self.deg_entry = tkinter.Entry(self.top_frame, width=10)

        # Pack the top frame's widgets
        self.prompt_label.pack(side='left')
        self.deg_entry.pack(side='left')

        # Create the widgets for the middle frame.
        self.descr_label = tkinter.Label(self.mid_frame,
                                         text='Degrees in Fahrenheit:')

        # Create a stringvar object to link with the output label.
        self.value = tkinter.StringVar()

        # Create the label for the stringvar.
        self.deg_F_label = tkinter.Label(self.mid_frame,
                                         textvariable=self.value)

        # Create the widgets for the middle frame.
        self.descr_label2 = tkinter.Label(self.mid_frame2,
                                          text='Degrees in Celsius:')

        # Create a stringvar object to link with the output label.
        self.value2 = tkinter.StringVar()

        # Create the label for the stringvar.
        self.deg_F_label2 = tkinter.Label(self.mid_frame2,
                                          textvariable=self.value2)

        # Pack the middle frame2's widgets.
        self.descr_label2.pack(side='left')
        self.deg_F_label2.pack(side='left')

        # Pack the middle frame's widgets.
        self.descr_label.pack(side='left')
        self.deg_F_label.pack(side='left')

        # Create the button widgets for the bottom frame.
        self.calcC_button = tkinter.Button(self.bottom_frame,
                                           text='Conevert to C', command=self.convert_C)
        self.calcF_button = tkinter.Button(self.bottom_frame,
                                           text='Conevert to F', command=self.convert_F)
        self.quit_buttom = tkinter.Button(self.quit_frame,
                                          text='Quit', command=self.main_window.destroy)

        # Pack the buttons.
        self.calcC_button.pack(side='left')
        self.calcF_button.pack(side='right')
        self.quit_buttom.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.mid_frame2.pack()
        self.bottom_frame.pack()
        self.quit_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The convert method is a callback function for the calculate button.
    def convert_F(self):
        # Get the valued entered by the user from kilo_entry.
        deg = float(self.deg_entry.get())

        # Convert Celcius to Fahrenheit.
        degF = (9/5) * deg + 32

        # Convert Fahrenheit to a string and store in the stringvar object.
        self.value.set(degF)

        clear = ' '
        self.value2.set(clear)

     # The convert method is a callback function for the calculate button.
    def convert_C(self):
        # Get the valued entered by the user from kilo_entry.
        deg = float(self.deg_entry.get())

        # Convert Celcius to Fahrenheit.
        degC = (deg - 32) * 5/9

        # Convert Fahrenheit to a string and store in the stringvar object.
        self.value2.set(degC)

        clear = ' '
        self.value.set(clear)


# Create an instance of the KiloConverterGUI class.
TempCal = TempCalculation()
