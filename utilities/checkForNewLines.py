import getpass
import followPath
import getWhoList
import parseWhoList

def checkForNewLines():
    username = getpass.getuser()
    path = f"C:\\Users\\{username}\\.lunarclient\\logs\\launcher\\renderer.log"
    logfile = open(path, "r")
    loglines = followPath.followPath(logfile)
    for line in loglines:
        whoList = getWhoList.getWhoList(line)
        if whoList:
            print(parseWhoList.parseWhoList(whoList))