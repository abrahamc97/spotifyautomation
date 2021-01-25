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
if today.day == 1:
    sp= createSpotifyEnv(spotify_user_id,spotify_token)
    name= makePlaylistName()
    print(name)
    desc= makeInspirationalQuote()
    makeMonthlyPlaylist(sp,username,name,desc)
    monthlyurl= getMonthURL(sp, username, name)
    print(monthlyurl)
    sample_texts = ["Please bless this playlist with some music: ", "Here you go humans: ", "No, it's not Christmas, but here's a playlist: ", "It's about that time again: ", "You know what to do: ", "I need some new groovy tunes: ", "I need 100cc of new music. Stat!: ", "My doctor said music should help my grumpiness. Help me out: ", "I'll just leave this here: ", "Hear ye. Hear ye. I require music now please: ", "If you don't add music, I'm telling on you: ", "Neethu's mom said, 'Add music, or else.' You better listen to her: ", "This following message is from John. 'Here's a scrumptious playlist for y'all': ", "President Biden said it's your constitutional duty to add music to the playlist, soooo...: ", "I don't have anything creative to say this month. Here's this month's playlist: ", "Some of you are deficient in Vitamin Do, Re, and Mi. So here you go: ", "Richu says 'Add music to the playlist your cowards.': ", ""]
    text= random.choice(sample_texts)
    message_id=sendPlaylist(user_id, password, thread, text + monthlyurl)
    print(message_id)
d1= date.today()
year= d1.year
d2= date(year, 12, 31)
time.sleep(2)

if d1==d2:
    getYearURL(sp, username)
    sendPlaylist(user_id, password, thread, "Here's the playlist for the year: " + yrurl)
sys.stdout.close()
