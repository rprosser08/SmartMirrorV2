from tkinter import *
from date import Date

# Class to handle the GUI for the Smart Mirror
class MainFrame:
    def __init__(self):
        root = Tk()
        root.title("Smart Mirror")
        root.configure(background="black")
        root.attributes("-fullscreen", True)
        date_text = Label(root, text=Date.get_date())
        date_text.pack()
        time_text = Label(root, text=Date.get_time())
        time_text.pack()
        root.mainloop()



if __name__ == "__main__":
    MainFrame()