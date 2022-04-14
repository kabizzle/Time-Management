import json


class FileData:
    def __init__(self, filename):
       self.filename = filename
    
    def read_file(self):
        # try:
        with open(self.filename, 'a+') as file:  # open file
            file_data = json.load(file)
            return file_data

        # except OSError:    # if wrong filename inputted or file not present in directory
        #     raise FileNotFoundError("Incorrect file name: file not found")
    
