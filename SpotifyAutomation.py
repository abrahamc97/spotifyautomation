import os
import json
import sys
import time
import fbchat
import random
import spotipy
import datetime
import numpy as np
import pandas as pd

from api import *
from json import loads
from requests import get
from fbchat import Client
from datetime import date
from send_message import *
from fbchat.models import *
from create_playlist import *
from datetime import datetime
from flask import Flask, request
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from secrets import spotify_token, spotify_user_id,username, user_id, password, thread



today = datetime.now()
if today.day == 1:
sp= createSpotifyEnv(spotify_user_id,spotify_token)
name= makePlaylistName()
desc= makeInspirationalQuote()
makeMonthlyPlaylist(sp,username,name,desc)
monthlyurl= getMonthURL(sp, username, name)
sendPlaylist(user_id, password, thread, "Here's this month's playlist: " + monthlyurl)

d1= date.today()
year= d1.year
d2= date(year, 12, 31)
time.sleep(2)

if d1==d2:
    getYearURL(sp, username)
    sendPlaylist(user_id, password, thread, "Here's the playlist for the year: " + yrurl)
