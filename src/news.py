import requests
import os
from dotenv import load_dotenv
import logging


# Class responsible for handling the news API calls
class News:
    def news_api_call():
        # Set up logger
        logging.basicConfig(filename='/tmp/smartmirror.log', level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')
        logger = logging.getLogger(__name__)

        load_dotenv()
        NYT_API_KEY = os.getenv("NYT_API_KEY")
        articles = []

        try:
            r = requests.get(f"https://api.nytimes.com/svc/topstories/v2/home.json?api-key={NYT_API_KEY}")
            r.raise_for_status()
            response = r.json()

            try:
            # Get the articles necessary information
                for article in response['results']:
                    info = {}
                    info['title'] = article['title']
                    info['abstract'] = article['abstract']
                    articles.append(info)
            except KeyError:
                return []

        except requests.exceptions.HTTPError as errh:
            logger.error(errh)
        except requests.exceptions.ConnectionError as errc:
            logger.error(errc)
        except requests.exceptions.Timeout as errt:
            logger.error(errt)
        except requests.exceptions.RequestException as err:
            logger.error(err)

        return articles
