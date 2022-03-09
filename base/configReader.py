import json


class Configuration:
    """reads & provides the Configuration file"""

    def __init__(self, path: str):
        self.config = None
        self.path = path

    def load(self):
        """loads the json file"""
        with open(self.path) as config_file:
            self.config = json.load(config_file)

    def __getitem__(self, item):
        return self.config[item]
