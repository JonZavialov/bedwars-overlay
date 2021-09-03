import json

def read(path):
    with open(path, 'r') as openfile:
        json_object = json.load(openfile)
    
    return json_object