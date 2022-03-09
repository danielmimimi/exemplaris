import logging
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

    def upload_blob_to_s3(self, path_to_data: str):
        """Copies data to S3 bucket and returns storage adress"""
        raise NotImplementedError

    def insert_data_into_database(self, info_extractor_name: str, result: str,
                                  blob_path: str):
        """Sends the data to the restAPI"""
        data = {  # noqa:F841
            "proc_Name": info_extractor_name,
            "timestamp": datetime.now().time() * 1000,
            "result": result,
            "link": blob_path
        }
        raise NotImplementedError
