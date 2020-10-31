import os
import json
import sys
import time
import spotipy
import datetime
import numpy as np
import pandas as pd

from json import loads
from requests import get
from datetime import date
from secrets import spotify_token, spotify_user_id, user_id
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


#Authorization and Client Credentials
scopes= "user-read-private user-read-email playlist-read-collaborative playlist-modify-public playlist-modify-private user-library-modify user-follow-modify ugc-image-upload"
sp= spotipy.Spotify(auth_manager=SpotifyOAuth(spotify_user_id, spotify_token,'http://127.0.0.1:5000/spotify/callback', scope=scopes))

# #Playlist Name
# name= date.today().strftime("%m.%y").lower()
#
# #Inspirational quote playlist description
# response = get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
# res= json.loads(response.text)
# desc= res["quoteText"]+ " - " + res["quoteAuthor"]
#
#
# #Create monthly playlist
# sp.user_playlist_create(user_id,name,public= False,collaborative=True, description= desc)

d1= date.today()
year= d1.year
d2= date(year, 10, 31)

time.sleep(2)

if d1==d2:
    response = get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
    res= json.loads(response.text)
    desc= res["quoteText"]+ " - " + res["quoteAuthor"]
    yrname=date.today().strftime("'%y")
    sp.user_playlist_create(user_id, yrname , public= True ,description=desc)

    allplaylists = sp.user_playlists(user_id)
    names=[]
    yr=date.today().strftime(".%y")
    for i, item in enumerate(allplaylists['items']):
        if item['name'].endswith(yr):
            names.append(item['id'])

    songs=[]
    for playlistid in names:
        a= sp.playlist_items(playlistid, fields='items.track.uri')
        for song in a['items']:
            songs.append(song.get('track').get('uri'))

    yrid=[]
    for i, item in enumerate(allplaylists['items']):
        if item['name'].endswith(yrname):
            yrid=item['id']

    sp.playlist_add_items(yrid, songs)
