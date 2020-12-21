import os
import json
import sys
import time
import fbchat
import random
import spotipy
import datetime
import pandas as pd

from json import loads
from requests import get
from fbchat import Client
from datetime import date
from send_message import *
from fbchat.models import *
from create_playlist import *
from datetime import datetime
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from secrets import spotify_token, spotify_user_id, username, user_id, password, thread

sys.stdout = open("History.txt", "a")
today = datetime.now()
print('New Entry')
print(today)
if today.day == 19:
    sp= createSpotifyEnv(spotify_user_id,spotify_token)
    name= makePlaylistName()
    print(name)
    desc= makeInspirationalQuote()
    makeMonthlyPlaylist(sp,username,name,desc)
    monthlyurl= getMonthURL(sp, username, name)
    print(monthlyurl)
    message_id=sendPlaylist(user_id, password, thread, "Here's this month's playlist: " + monthlyurl)
    print(message_id)
d1= date.today()
year= d1.year
d2= date(year, 12, 31)
time.sleep(2)

if d1==d2:
    getYearURL(sp, username)
    sendPlaylist(user_id, password, thread, "Here's the playlist for the year: " + yrurl)
sys.stdout.close()
