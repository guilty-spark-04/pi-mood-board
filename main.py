import vlc
from time import sleep
import os
from flask import Flask
import pafy


app = Flask(__name__)

Instance = vlc.Instance('--fullscreen','--input-repeat=999999','--mouse-hide-timeout=0')
player = Instance.media_player_new()



def play(path):
    global player
    Media = Instance.media_new(path)
    player.set_media(Media)
    Media.get_mrl()
    player.set_fullscreen(True)
    player.play()
def playOnline(url):
    global player
    video = pafy.new(url)
    best = video.getbest()
    Media = Instance.media_new(best.url)
    player.set_media(Media)
    Media.get_mrl()
    player.set_fullscreen(True)
    player.play()
def stop():
    global player
    player.stop()


@app.route('/')
def test():
    return "Howdy world"

@app.route('/vibeone')
def vibe_1():
    play("./clips/bebop.mkv")
    return 'done'

@app.route('/demon')
def vibe_3():
    play("./clips/demon.mp4")
    return 'done'

@app.route('/eva')
def vibe_2():
    play("./clips/eva.mp4")
    return 'done'

@app.route("/jjk")
def jjk():
    play("./clips/jjk.mp4")
    return 'done'

@app.route("/space")
def space():
    playOnline("https://www.youtube.com/watch?v=0k23DVv_xsA")
    return 'done'
play("/clips/eva.mp4")
app.run(host='0.0.0.0',port=5000)