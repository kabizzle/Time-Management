import json


class FileData:
    def __init__(self, filename):
       self.filename = filename
    
    @staticmethod
    def read_file(filename):
        try:
            with open(filename, 'r') as file:  # open file
                file_data = json.loads(file.read())
                return file_data
        except OSError:    # if wrong filename inputted or file not present in directory
            raise FileNotFoundError("Incorrect file name: file not found")
    
    def write_to_file(self, json_data):
        with open(self.filename, "a+") as file:
            file.write(json.dumps(json_data, indent=4))
    
