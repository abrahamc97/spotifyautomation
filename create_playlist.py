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
from secrets import spotify_token, spotify_user_id, username
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


#Authorization and Client Credentials
def createSpotifyEnv(spotify_user_id, spotify_token):
    scopes= "user-read-private user-read-email playlist-read-collaborative playlist-modify-public playlist-modify-private user-library-modify user-follow-modify ugc-image-upload"
    sp= spotipy.Spotify(auth_manager=SpotifyOAuth(spotify_user_id, spotify_token,'http://127.0.0.1:5000/spotify/callback', scope=scopes))
    return sp

#Playlist Name
def makePlaylistName():
    name= date.today().strftime("%m.%y").lower()
    return name

#Inspirational quote playlist description
def makeInspirationalQuote():
    response = get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
    res= json.loads(response.text)
    desc= res["quoteText"]+ " - " + res["quoteAuthor"]
    return desc


#Create monthly playlist
def makeMonthlyPlaylist(sp, username,name,desc):
    monthpl= sp.user_playlist_create(username,name,public= True, description= desc)
    return

def getMonthURL(sp, username, name):
    allplaylists = sp.user_playlists(username)
    monthlyid=''
    monthlyurl=''
    for i, item in enumerate(allplaylists['items']):
        if item['name'].endswith(name):
            monthlyid=item['id']
            monthlyurl=item['external_urls'].get('spotify')
    sp.playlist_change_details(monthlyid, public=False, collaborative=True)
    return monthlyurl

# Create yearly playlist
# d1= date.today()
# year= d1.year
# d2= date(year, 12, 31)
#
# time.sleep(2)
#
# if d1==d2:
def getYearURL(sp, username):
    response = get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
    res= json.loads(response.text)
    desc= res["quoteText"]+ " - " + res["quoteAuthor"]
    yrname=date.today().strftime("'%y")
    sp.user_playlist_create(username, yrname , public= True ,description=desc)

    allplaylists = sp.user_playlists(username)
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

    yrid=""
    yrurl=""
    for i, item in enumerate(allplaylists['items']):
        if item['name'].endswith(yrname):
            yrid=item['id']
            yrurl=item['external_urls'].get('spotify')

    sp.playlist_add_items(yrid, songs)

    return yrurl
