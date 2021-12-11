from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/")
def home():
  return "temb.glitch.me - github.com/zxmp/temb"

def runhost():
  app.run(host="0.0.0.0",port=8000)
  
def run(bool):
  if bool == True:
    t = Thread(target=runhost)
    t.start()
  else:
    print("INFO: You Power Off The Host. dont use a uptimerobot now.")
