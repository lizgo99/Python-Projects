from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
link = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(link)
billboard_webpage = response.text
soup = BeautifulSoup(billboard_webpage, "html.parser")

billboard_songs = []
for e in soup.find_all(attrs={'class':'o-chart-results-list-row-container'}):    
    billboard_songs.append({
        'title':e.h3.get_text(strip=True),
        'artist':e.h3.find_next('span').get_text(strip=True)
    })  
      
CLIENT_ID = "MY_CLIENT_ID"
CLIENT_SECRET = "MY_CLIENT_SECRET"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="my_user_name", 
    )
)
user_id = sp.current_user()["id"]

song_uris = []
for song in billboard_songs:
    if "Featuring" in song['artist']:
        i = song['artist'].index("Featuring")
        query = f"track:{song['title']} artist:{song['artist'][:(i-1)]}"
    else:    
        query = f"track:{song['title']} artist:{song['artist']}"
    
    result = sp.search(q=query, limit=1, type="track")
    tracks = result['tracks']['items']
    if tracks:
        uri = tracks[0]['uri']
        song_uris.append(uri)
    else:
        print(f"Couldn't find: {song['title']} - {song['artist']}")
        

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
playlist_id = playlist['id']
pprint.pprint(playlist_id)
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
