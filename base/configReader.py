
import json

class configuration():
    def __init__(self,path : str) :
        self.path = path

    def load(self):
        with open(self.path) as config_file:
            self.config = json.load(config_file)
