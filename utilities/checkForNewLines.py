import getpass
from utilities import followPath
from utilities import getWhoList
from utilities import parseWhoList
from jsonMethods import write

def checkForNewLines():
    username = getpass.getuser()
    path = f"C:\\Users\\{username}\\.lunarclient\\logs\\launcher\\renderer.log"
    logfile = open(path, "r")
    loglines = followPath.followPath(logfile)
    for line in loglines:
        whoList = getWhoList.getWhoList(line)
        if whoList:
            write.write("whoList.json",parseWhoList.parseWhoList(whoList))