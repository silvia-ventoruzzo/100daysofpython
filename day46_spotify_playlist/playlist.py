import os
from dotenv import load_dotenv
from pathlib import Path
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv(dotenv_path=Path('./twilio.env'))
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_USERNAME = os.getenv('SPOTIFY_USERNAME')

class Playlist:
    
    def __init__(self, 
                 client_id=SPOTIFY_CLIENT_ID, 
                 client_secret=SPOTIFY_CLIENT_SECRET, 
                 client_username=SPOTIFY_USERNAME,
                 redirect_uri="http://example.com"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_username = client_username
        self.redirect_uri = redirect_uri
    
    def authenticate(self):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id,
                                                       client_secret=self.client_secret,
                                                       redirect_uri=self.redirect_uri,
                                                       scope="playlist-modify-private",
                                                       show_dialog=True,
                                                       cache_path="token.txt",
                                                       username=self.redirect_uri))
        self.spotify = sp
        
    def create(self, name):
        user_id = self.spotify.me()['id']
        try:
            response = self.spotify.user_playlist_create(user_id, name, public=False) 
            self.playlist_id = response.get('id')
        except spotipy.exceptions.SpotifyException as e:
            print(e)
        else:
            print(f"Playlist {name} created.")
            
    def find_song_uri(self, title, artist):
        result = self.spotify.search(q=f"track: {title} artist: {artist}", type="track")
        try:
            return result["tracks"]["items"][0]["uri"]
        except ValueError:
            print(f'The song {title} by {artist} is not on Spotify')
            
    def add_songs(self, song_uris):
        try:
            self.spotify.user_playlist_add_tracks(user=self.client_id, 
                                                playlist_id=self.playlist_id, 
                                                tracks=song_uris)
        except Exception as e:
            print(e)
        else:
            print('Songs successfully added')