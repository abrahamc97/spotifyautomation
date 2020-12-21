# **Monthly Spotify Playlist Automation**
#### Welcome to my first project!

Since August 2019, my friends from college and I had would add music to a monthly Spotify playlist. It was a good way for us to discover new artists and keep in touch after graduation. Flash forward to October 2020, I had just finished a Python course on Udemy and bored out of my mind when my friend (s/o Jasmine) messages our group chat on Facebook with October's playlist. That's when the idea for this project was born.

As far as I can tell, there are four components to this project:
* Using Spotipy to create the playlists
* Using fbchat to send the playlist url to our group chat
* Creating a file handling script to run through all the functions
* Using Windows Task Scheduler to automate for the 1st of every month and on December 31

So let's jump into it.

###### Spotipy
* *api.py*\
    This file creates an endpoint of the redirect URL. This [Medium article](https://medium.com/@hmlon/explaining-how-oauth-works-with-spotify-as-an-example-f16547be4ff6) was really helpful in understanding the basics of Flask. api.py also contains a commented out portion that was used to setup a Facebook webhook on a server hosted by Heroku in case fbchat stopped working. This [Twilio article](https://www.twilio.com/blog/2017/12/facebook-messenger-bot-python.html) was incredibly detailed and easy for a beginner like me to follow along.

* *create_playlist.py*\
    Here's where the magic happens. In this file, I define six functions:
    1. Set up the OAuth token for Spotify
    2. Assign playlist name
    3. Generate an inspirational quote to be include in the description
    4. Create monthly playlists
    5. Get monthly playlist's URL
    6. Create annual playlist and return the URL

###### fbchat
* *send_message.py*\
    This file contains the function to send the playlist URLs to our group chat.

###### File handling
* *SpotifyAutomation.py*\
    This script contains the logic that creates the playlist on the first of the month. There is also "if statement" where on December 31st, we take all the songs in the monthly playlists and add them to the yearly playlist.

###### Windows Task Scheduler
  I followed this [article](https://datatofish.com/python-script-windows-scheduler/) to schedule api.py and SpotifyAutomation.py to run automatically

Last, but not least, I could not have completed this project without the help of my friend Jon Mathai. He's been incredibly patient and a great teacher. Here's a link to his [Github](https://github.com/jonm8116)
