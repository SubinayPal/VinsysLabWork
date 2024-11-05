import json
def readJsonFile(./Insulin/insulin.json):
    data = ""
    try:
        with open(insulin.json) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data