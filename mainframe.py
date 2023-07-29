from tkinter import *

# Class to handle the GUI for the Smart Mirror
class MainFrame:
    def __init__(self):
        root = Tk()
        root.title("Smart Mirror")
        root.configure(background="black")
        root.attributes("-fullscreen", True)
        root.mainloop()



if __name__ == "__main__":
    MainFrame()