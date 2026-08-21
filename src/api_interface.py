import os
import requests
from dotenv import load_dotenv

load_dotenv()

class TheMovieDatabase:
    api_url = os.getenv('API_URL')
    api_token = os.getenv('API_TOKEN')

    def __init__ (self):
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'Bearer {self.api_token}'})

    def return_total_pages(self):
        result = self.session.get(
            self.api_url,
            params={'page': 1}
        ).json()

        return result['total_pages']


    def return_movie_page(self, page_number: int):
        return self.session.get(
                self.api_url,
                params={'page': page_number},
                timeout=10
        )