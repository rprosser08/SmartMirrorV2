from tkinter import *
from date import Date

# Class to handle the GUI for the Smart Mirror
class MainFrame:
    def __init__(self):
        self.root = Tk()
        self.root.title("Smart Mirror")
        self.root.configure(background="black")
        self.root.attributes("-fullscreen", True)

        # Date Label
        self.date_text = Label(self.root)
        self.date_text.pack()
        self.get_date()

        # Time Label
        self.time_text = Label(self.root)
        self.time_text.pack()
        self.get_time()


        self.root.mainloop()

    
    # Responsible for updating the current date every 500ms
    def get_date(self):
        self.date_text.configure(text=Date.get_date())
        self.date_text.after(500, self.get_date)

    
    # Responsible for updating the current time every 500ms
    def get_time(self):
        self.time_text.configure(text=Date.get_time())
        self.time_text.after(500, self.get_time)




if __name__ == "__main__":
    MainFrame()