import lyricsgenius
genius = lyricsgenius.Genius("Va0VIqT294-NAWwQxY0dqbxpzEumHobeG1xX0RJu3efOBQdumiJZsv7jr9Itt9ep")
from pprint import pprint
import re

def get_song(song_name, artist_name):
    song = genius.search_songs(f"{song_name} by {artist_name}")

    fin = []
    for res in song["hits"]:
        if res["result"]["primary_artist"]["name"].lower() == artist_name.lower() and bool(re.search(song_name.lower(), res["result"]["full_title"].lower())):
            fin.append(res["result"])
    
    return fin


def get_lyrics(song_name, artist_name):
    try:
        song_ids = [sng['id'] for sng in get_song(song_name, artist_name)]
    except:
        raise Exception("Song doesn't exist!")

    lyrics = [genius.lyrics(song_id=song_id) for song_id in song_ids]
    songs = [genius.song(song_id=song_id) for song_id in song_ids]
    
    return [(lyric, song) for lyric, song in zip(lyrics, songs)]






