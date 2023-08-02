from tkinter import *
from PIL import ImageTk, Image
from date import Date
from weather import Weather
from news import News


# Class to handle the GUI for the Smart Mirror
class MainFrame:
    def __init__(self):
        self.root = Tk()
        self.root.title("Smart Mirror")
        self.root.configure(background="black", cursor="none")
        self.root.attributes("-fullscreen", True)

        # Cause screen to update width and height if necessary
        self.root.update_idletasks()
        self.screen_width = self.root.winfo_width()
        self.screen_height = self.root.winfo_height()

        # Configure the column weights(widths)
        self.root.columnconfigure(0, weight=1, uniform='column')
        self.root.columnconfigure(1, weight=1, uniform='column')

        # Configure the row weights(lengths)
        self.root.rowconfigure(0, weight=8, uniform='row')
        self.root.rowconfigure(1, weight=1, uniform='row')
        self.root.rowconfigure(2, weight=1, uniform='row')

        # Date and Time Label
        self.date_text = Label(self.root, background='black', foreground='white', font=("Arial", 25))
        self.date_text.grid(row=0, column=0, sticky='nw')
        self.get_date()

        # Weather Label
        self.weather_text = Label(self.root, compound="left", background='black', foreground='white', font=("Arial", 25))
        self.weather_text.grid(row=0, column=1, sticky='ne')
        self.get_weather()

        # News Label
        self.news_title_text = Label(self.root, background="black", foreground="white", wraplength=self.screen_width // 2, font=("Arial", 25))
        self.news_title_text.grid(row=1, column=0, columnspan=2, sticky='sew')
        self.news_abstract_text = Label(self.root, background="black", foreground="white", wraplength=self.screen_width // 2)
        self.news_abstract_text.grid(row=2, column=0, columnspan=2, sticky='new')
        self.get_news()

        self.root.mainloop()

    
    # Responsible for updating the current date and time every 500ms
    def get_date(self):
        self.date_text.configure(text=Date.get_date() + "\n" + Date.get_time())
        self.date_text.after(500, self.get_date)


    # Responsible for updating the current weather every 1 minute
    def get_weather(self):
        # Get weather info
        weather = Weather.weather_api_call()

        if weather:
            self.weather_info = weather

            # Prepare the image for the tkinter label
            icon = Image.open(self.weather_info[0])
            weather_icon = ImageTk.PhotoImage(icon)

            # Place weather icon and weather temperature in the label
            self.weather_text.configure(image=weather_icon, text=self.weather_info[1])
            # Prevent garbage collection from collecting the weather icon
            self.weather_text.image = weather_icon
        
        self.weather_text.after(60000, self.get_weather)


    # Responsible for getting the news articles information and resetting the counter
    def get_news(self):
        articles = News.news_api_call()
        if articles:
            self.news_articles = articles

        self.i = 0
        self.update_news()

    # Responsible for updating which news articles are showing
    def update_news(self):
        self.news_title_text.configure(text=self.news_articles[self.i]['title'])
        self.news_abstract_text.configure(text=self.news_articles[self.i]['abstract'])
        self.i += 1

        # If there are more articles to show, show the next article in the list
        # Otherise make another API call
        if self.i < len(self.news_articles):
            self.news_title_text.after(30000, self.update_news)
        else:
            self.news_title_text.after(30000, self.get_news)

if __name__ == "__main__":
    MainFrame()