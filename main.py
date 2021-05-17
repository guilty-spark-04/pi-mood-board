import vlc
from time import sleep
import os
from flask import Flask


app = Flask(__name__)

Instance = vlc.Instance('--fullscreen','--input-repeat=1','--mouse-hide-timeout=0')
player = Instance.media_player_new()



def play(path):
    global player
    Media = Instance.media_new(path)
    player.set_media(Media)
    Media.get_mrl()
    player.set_fullscreen(True)
    player.play()
    sleep(5)
    while player.is_playing():
        sleep(1)

def stop():
    global player
    player.stop()

play("./clips/vibes.mkv")
@app.route('/')
def test():
    return "Howdy world"
@app.route('/vibeone')
def vibe_1():
    play("./clips/vibes.mkv")
    return 'done'
@app.route('/stop')
def end():
    stop()
    return 'done'
