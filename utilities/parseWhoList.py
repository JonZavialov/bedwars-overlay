def parseWhoList(line):
    names = []
    count = 1
    
    for i in line:
        if i == ',':
            count = count + 1

    while count != 0:
        if count == 1:
            name = line
        else:
            name = line[0:line.index(", ")]
            line = line[line.index(", ")+2:len(line)]
        count -= 1
        names.append(name.strip())

    return names