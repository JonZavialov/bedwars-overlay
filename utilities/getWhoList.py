def getWhoList(line):
    if "[CHAT] ONLINE: " in line:
        return (line[line.index("ONLINE: ") + 8 : -1])