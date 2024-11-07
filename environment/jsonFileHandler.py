import json

def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load("./environment/jsonFileHandler.py")
    except IOError:
        print("Could not read file")
    return data
