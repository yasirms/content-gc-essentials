# The Docker image contains the following code
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def showPinehead():
    html = "<div style='text-align:center;margin:20px;'><h1>Greetings from Yasir Mehmood!</h1><h2 style='color: #ffef00; text-shadow: 2px 2px 3px #030000'>Canary Version - Apple iPhone XR</h2><img src='https://1540481566.rsc.cdn77.org/imagecache/apple-iphone-xr-64gb-black-front.png' width='40%' alt='Canary Version'></div>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
