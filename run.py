import os

from youtube_client import YouTubeClient
from spotify_client import SpotifyClient


def validate(message):
    while True:
        val = input(message)
        try:
            val = int(val)
            print("Please enter a valid number")
        except ValueError:
            return val


def run():
    # 1. Get a list of our playlist from YouTube
    youtube_client = YouTubeClient('./creds/client_secret.json')
    spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
    playlists = youtube_client.get_playlist()

    # 2. Ask which playlist they want to get songs from
    for index, playlist  in enumerate(playlists):
        print(f'{index}: {playlist.title}')
    choice = validate("Which Playlist: ")
    chosen_playlist = playlists[choice]
    print(f"You've selected: {chosen_playlist.title}")

    #3. For each video in playlist get the song information
    songs = youtube_client.get_song_info_from_video(chosen_playlist.id)
    print(f"Attempting to add {len[songs]}")

    # Search for songs on spotify
    for song in songs:
        spotify_song_id = spotify_client.search_song(song.artist, song.track)
        if spotify_song_id:
            added_song = spotify_client.add_song_to_spotify(spotify_song_id)
            if added_song:
                print(f"Added {song.artist}")

if __name__ == '__main__':
    run()
