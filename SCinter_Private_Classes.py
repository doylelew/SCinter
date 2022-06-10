# These Classes are support Classes not meant to be called by the End User

from tkinter import Tk, Frame

# Frame meant for drawing the base most window and naming that window.
# This frame created in the mainframe and runs it's mainloop() method on Mainframe's start() method
class ProgramWindow(Tk):

    # creates the title and window size in the __init__ method
    def __init__(self, title, width, height):
        super().__init__()
        self.title(title)
        self.resize(width, height)

    # can be called at any time to change the ProgramWindow width and height
    def resize(self, width, height):
        # find the center point
        center_x = int(self.winfo_screenwidth() / 2 - width / 2)
        center_y = int(self.winfo_screenheight() / 2 - height / 2)

        self.geometry(f'{width}x{height}+{center_x}+{center_y}')

# A base class all other frames will inherit from
class SCFrame(Frame):
    # a shared variable for all frames where information can be sotred to be called in other frames
    _app_data = {}

    # CRUD functions for storing data in the shared _app_data variable
    def store(key, value):
        SCFrame._app_data[key] = value

    def retrieve(key):
        return SCFrame._app_data[key]

    def release(key):
        del SCFrame._app_data[key]









