import vlc
from time import sleep
import os
from flask import Flask


app = Flask(__name__)

@app.route('/')
def test():
    return "Howdy world"