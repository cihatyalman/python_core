from Core.json_file_operations.json_file_base import JsonFileBase

class JsonFileDemo(JsonFileBase):
    def __init__(self):
        super().__init__("UI/json_file/demo.json")
