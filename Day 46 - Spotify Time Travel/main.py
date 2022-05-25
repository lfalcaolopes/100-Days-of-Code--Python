import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

song_names_spans = soup.find_all("h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
                                              "lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 "
                                              "u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 "
                                              "u-max-width-230@tablet-only")
song_list = [song.getText().replace('\n', '') for song in song_names_spans]

print(song_list)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        # client_id="https://developer.spotify.com/dashboard/applications",
        # client_secret="https://developer.spotify.com/dashboard/applications",
    )
)

# user_id = "https://www.spotify.com/br/account/overview/?utm_source=spotify&utm_medium=menu&utm_campaign=your_account"

uri_list = [sp.search(q=songs, limit=1, market="BR")["tracks"]["items"][0]["uri"] for songs in song_list]

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, description="Created by code")

sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list, position=None)



