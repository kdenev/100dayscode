import sys
import os
# Import api script
sys.path.append(r"D:\Desktop\code\python\api_key_creator")
import api_key_creator
import requests

class TMDBMovie:
    def __init__(self) -> None:
        self.headers = {
            "accept": "application/json",
            "Authorization": os.environ['TMDB_API_AUTH']
        }

    def fetch_movie_list(self, title):
        self.url = "https://api.themoviedb.org/3/search/movie"
        self.params = {
            "query": title
        }
        response = requests.get(self.url , headers=self.headers, params=self.params)
        
        return response.json()['results'] or None
