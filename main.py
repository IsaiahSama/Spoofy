from dotenv import load_dotenv

load_dotenv()
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

i = 0
results = sp.current_user_saved_tracks(50)
while results["items"]:
    for idx, item in enumerate(results["items"], start=50 * i):
        track = item["track"]
        print(idx, track["artists"][0]["name"], " – ", track["name"])
    i += 1
    results = sp.current_user_saved_tracks(50, 50 * i)
