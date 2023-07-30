from tkinter import *
from PIL import ImageTk, Image
from date import Date
from weather import Weather


# Class to handle the GUI for the Smart Mirror
class MainFrame:
    def __init__(self):
        self.root = Tk()
        self.root.title("Smart Mirror")
        self.root.configure(background="black")
        self.root.attributes("-fullscreen", True)
        self.screen_width = self.root.winfo_width()
        self.screen_height = self.root.winfo_height()

        # Configure the column weights(widths)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        # Date and Time Label
        self.date_text = Label(self.root, background='black', foreground='white', font=("Arial", 25))
        self.date_text.grid(row=0, column=0, sticky='nw')
        self.get_date()

        # Weather Label
        self.weather_text = Label(self.root, compound="left", background='black', foreground='white', font=("Arial", 25))
        self.weather_text.grid(row=0, column=1, sticky='ne')
        self.get_weather()

        self.root.mainloop()

    
    # Responsible for updating the current date and time every 500ms
    def get_date(self):
        self.date_text.configure(text=Date.get_date() + "\n" + Date.get_time())
        self.date_text.after(500, self.get_date)


    # Responsible for updating the current weather every 1 minute
    def get_weather(self):
        # Get weather info
        weather_info = Weather.weather_api_call()

        # Prepare the image for the tkinter label
        icon = Image.open(weather_info[0])
        weather_icon = ImageTk.PhotoImage(icon)

        # Place weather icon and weather temperature in the label
        self.weather_text.configure(image=weather_icon, text=weather_info[1])
        # Prevent garbage collection from collecting the weather icon
        self.weather_text.image = weather_icon
        
        self.weather_text.after(60000, self.get_weather)




if __name__ == "__main__":
    MainFrame()