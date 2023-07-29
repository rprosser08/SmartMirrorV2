from tkinter import *
from date import Date

# Class to handle the GUI for the Smart Mirror
class MainFrame:
    def __init__(self):
        self.root = Tk()
        self.root.title("Smart Mirror")
        self.root.configure(background="black")
        self.root.attributes("-fullscreen", True)
        self.get_date()
        self.get_time()
        self.root.mainloop()

    
    def get_date(self):
        date_text = Label(self.root, text=Date.get_date())
        date_text.pack()

    
    def get_time(self):
        time_text = Label(self.root, text=Date.get_time())
        time_text.pack()



if __name__ == "__main__":
    MainFrame()