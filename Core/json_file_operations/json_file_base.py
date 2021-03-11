import json
import os

class JsonFileBase:
    def __init__(self,path:str):
        "path: file path must end with (.json, .txt, .data, .cybox)"
        assert(path.endswith(".json") or path.endswith(".txt") or path.endswith(".data") or path.endswith(".cybox"))
        self.path = path

    def write(self,json_data):
        "json_data: Type, must be dict or list."
        assert(type(json_data) is dict or type(json_data) is list)
        with open(self.path,"w") as file:
            json.dump(json_data,file)

    def read(self):
        with open(self.path,"r") as file:
            return json.load(file)

    def delete(self):
        os.remove(self.path)

"""
json.loads(string)      : string -> json
json.dumps(json)        : json -> string

json.load(file)         : file -> json
json.dump(json,file)    : json -> file
"""
