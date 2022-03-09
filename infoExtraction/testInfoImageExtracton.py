import stomp
import json
from base.configReader import configuration
from base.infoExtractor import infoExtractor
from utils.imageConverter import imageConverter

class testInfoImageExtracton(infoExtractor,stomp.ConnectionListener):
    """test to visualize concept"""
    def __init__(self, config: configuration):
        super().__init__(config)
        self.subscriber.setListener(self.config['name'],self)

    def on_error(self, headers):
        """callback when topic receives an error"""
        print(headers)

    def on_message(self, headers):
        """callback when topic receives data"""
        converter =  imageConverter()
        extractedImage = converter.imageDecode(json.loads(headers.body))
