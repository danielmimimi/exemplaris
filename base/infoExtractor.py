import logging
import json
from base.configReader import Configuration
from datetime import datetime
from base.subscriber import Subscriber


class InfoExtractor:
    """Base class for information extraction"""

    def __init__(self, config: Configuration):
        self.config = config.config
        # TODO figure out if logging requires an instance to be held
        logging.basicConfig(
            level=logging.DEBUG, filename=config.config['name'] + '.log')
        self.subscriber = Subscriber(self.config, None)  # FIXME

    def uploadBlobToS3(self, pathToData : str):
        """Copies data to S3 bucket and returns storage adress"""
        raise NotImplementedError

    def insertDataIntoDatabase(self, infoExtractorName : str, result : str, blobPath : str):
        """Sends the data to the restAPI"""
        data = {
            "proc_Name":infoExtractorName,
            "timestamp": datetime.now().time() * 1000,
            "result": result,
            "link":blobPath
        }
        raise NotImplementedError




