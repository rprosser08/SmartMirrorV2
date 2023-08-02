from datetime import datetime
import pytz

# Class is responsible for getting the current date and time
class Date:
    # Returns the current date
    def get_date():
        time_zone = pytz.timezone('US/Eastern')
        current_date = datetime.now(time_zone).strftime("%A, %B %-d, %Y")
        return current_date


    # Returns the current time
    def get_time():
        time_zone = pytz.timezone('US/Eastern')
        current_time = datetime.now(time_zone).strftime("%-I:%M %p")
        return current_time
