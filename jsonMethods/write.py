import json

def write(path, dictionary):
    json_object = json.dumps(dictionary, indent = 4)
    print("writing", json_object)
    
    with open(path, "w") as outfile:
        outfile.write(json_object)