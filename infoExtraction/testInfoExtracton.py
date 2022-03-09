import stomp
from base.configReader import Configuration
from base.infoExtractor import InfoExtractor


class testInfoExtracton(InfoExtractor, stomp.ConnectionListener):
    """test to visualize concept"""

    def __init__(self, config: Configuration):
        super().__init__(config)
        self.subscriber.setListener(self.config['name'], self)

    def on_error(self, headers):
        """callback when topic receives an error"""
        print(headers)

    def on_message(self, headers):
        """callback when topic receives data"""
        print(headers)
