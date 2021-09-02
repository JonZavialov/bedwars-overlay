from utilities import checkForNewLines
import runApp
from threading import Thread

Thread(target=checkForNewLines.checkForNewLines).start()
Thread(target=runApp.runApp).start()