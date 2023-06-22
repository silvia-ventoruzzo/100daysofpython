from billboard import Billboard
from playlist import Playlist

billboard = Billboard()
playlist = Playlist()
playlist.authenticate()

billboard.ask_for_date()
billboard.get_top_100()

playlist.create(name=f"{billboard.user_response} Billboard 100")
song_list = []
print("Searching songs")
for song in billboard.songs.values():
    uri = playlist.find_song_uri(title=song.get('title'),
                                 artist=song.get('artist'))
    song_list.append(uri)
playlist.add_songs(song_list)