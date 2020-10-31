from flask import Flask

app = Flask(__name__)

@app.route("/spotify/callback")
def spotify_callback():
    return "You finally called me back!"
app.run()
