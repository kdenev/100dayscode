import sys
import os
# Import api script
sys.path.append(r"D:\Desktop\code\python\api_key_creator")
import api_key_creator

import requests

url = "https://api.themoviedb.org/3/search/movie"

headers = {
    "accept": "application/json",
    "Authorization": os.environ['TMDB_API_AUTH']
}

params = {
    "query":"Matrix"
}

response = requests.get(url, headers=headers, params=params)

data = response.json()['results']
data[0]['release_date']