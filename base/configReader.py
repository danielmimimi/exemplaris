
import json

class configuration():
    """reads & provides the configuration file"""
    def __init__(self,path : str) :
        self.path = path

    def load(self):
        """loads the json file"""
        with open(self.path) as config_file:
            self.config = json.load(config_file)
