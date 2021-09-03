from utilities import checkForNewLines
from utilities import openBrowser
from threading import Thread
from flask import *
from jsonMethods import write
from jsonMethods import read
import json

write.write("whoList.json", [])

Thread(target=checkForNewLines.checkForNewLines).start()

app = Flask(__name__)

@app.route("/data")
def data():
    return json.dumps(read.read("whoList.json"))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/init")
def init():
    return render_template('init.html')

if __name__ == "__main__":
    openBrowser.openBrowser("http://localhost:5000/init")
    app.run(host='localhost')