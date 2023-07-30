import requests
import os
from dotenv import load_dotenv


# Class responsible for handling the news API calls
class News:
    def news_api_call():
        load_dotenv()
        NYT_API_KEY = os.getenv("NYT_API_KEY")
        response = requests.get(f"https://api.nytimes.com/svc/topstories/v2/home.json?api-key={NYT_API_KEY}").json()
        print(response)




if __name__ == "__main__":
    News.news_api_call()