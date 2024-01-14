from dotenv import load_dotenv

load_dotenv()
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from sele import download_songs_by_ids

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

i = 0
results = sp.current_user_saved_tracks(50)
while results["items"]:
    ids = []
    for idx, item in enumerate(results["items"], start=50 * i):
        track = item["track"]
        track_id = track["id"]
        ids.append(track_id)

    download_songs_by_ids(ids)

    i += 1
    results = sp.current_user_saved_tracks(50, 50 * i)
