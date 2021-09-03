from utilities import checkForNewLines
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

if __name__ == "__main__":
    app.run(host='localhost')