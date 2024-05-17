from bs4 import BeautifulSoup
import requests
import spotipy

date = '2000-08-13'

doc = requests.get("https://www.billboard.com/charts/hot-100/" + date)
dochtml = doc.text
songs_100 = []
soup = BeautifulSoup(dochtml, 'html.parser')


songs_100_elements = soup.select("li ul li h3")

for song_element in songs_100_elements:
    songs_100.append(song_element.getText().strip())

print(songs_100)

client_id = "c7b8534e295947b7a79a572e22acd7f8"
client_secret = "a60c7413e4e84c6fb81f77a9301c66b5"



spotify = spotipy.oauth2.SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri="http://example.com", state=None, scope="playlist-modify-private", cache_path="day 46/token.txt", username="ckziait0kbll0atiy9kg1gpb7", proxies=None, show_dialog=True, requests_session=True, requests_timeout=None)


sp = spotipy.Spotify(auth_manager=spotify)

user_id = sp.current_user()["id"]

print(user_id)

#come back to this project!