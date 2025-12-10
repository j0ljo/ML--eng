import Spotipy_api_test
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

# Credentials (replace with your actual credentials)
CLIENT_ID = 'fff848ab47af4367a532654c834f4a19'
CLIENT_SECRET = '09e9a1bfaa564196a56540ce5368613f'

# Authenticate
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# API call to get an artist's albums

artist_name = "Kendrick Lamar"
print(f"Searcing for artist: {artist_name}...")

# sp.search is the Spotipy method to search for an item
results = sp.search(q='artist:' + artist_name, type='artist', limit = 1)

# API testing
if results and results['artists']['items']:
    artist = results['artists']['items'][0]
    artist_id = artist['id']
    print(f"Found artist: {artist['name']} with ID: {artist_id}")

    # Get the artist's albums
    albums = sp.artist_albums(artist_id, album_type='album')
    print(f"Albums by {artist_name}:")
    for album in albums['items']:
        print(f"- {album['name']} ({album['release_date']})")

        # Print a confirmation message
        print("\n API call successful. (200 0K equivalent)")
        print(f"Found Artist: {artist["name"]}")

        # Print key data points
        print(f"Spotify ID: {artist['id']}")
        print(f"followers: {artist['followers']['total']}")
        print(f"Genres: {', '.join(artist['genres'])}")

        # Print the full json response for inspection (Crucial for API testing)
        print(" Full JSON response:")
        print(json.dumps(artist, indent=4))


    else:
        print(f"No artist found for {artist_name}.")
        print