# The Docker image contains the following code
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def showPinehead():
    html = "<div style='text-align:center;margin:20px;'><h1>Greetings from Yasir Mehmood!</h1><h2>Stable Version</h2><img src='https://1540481566.rsc.cdn77.org/imagecache/samsung-galaxy-s10e-128gb-prism-black-front-20190520144320.png' width='40%' alt='Stable Version'></div>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
