import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import sys
import os

# Import api script
sys.path.append(r"D:\Desktop\code\python\api_key_creator")
import api_key_creator

user_date = input("Let's go back in time baby! Type the date in this format YYYY-MM-DD") or "2010-07-28"
url = f"https://www.billboard.com/charts/hot-100/{user_date}"
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
top100_songs = [row.find(name="h3", id="title-of-a-story").getText().strip() for row in soup.find_all(name="div", class_="o-chart-results-list-row-container")]


credentials = SpotifyOAuth(scope='playlist-modify-private')

sp = spotipy.Spotify(auth_manager=credentials)
me = sp.current_user()
top100_songs_sp_ids = [sp.search(song)['tracks']['items'][0]['id'] for song in top100_songs]
playlist = sp.user_playlist_create(me['id'], f"{user_date} Bilboard 100", False)
sp.playlist_add_items(playlist['id'], top100_songs_sp_ids)