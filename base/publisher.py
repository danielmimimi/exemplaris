import logging
from base.configReader import Configuration

from base.pubSubBase import PubSubBase


class Publisher(PubSubBase):
    """
    Handles the publishing of different kind of data
    """

    def __init__(self, config: Configuration, logger: logging):
        PubSubBase.__init__(self, config)
        self.logger = logger

    def publish(self, data: str):
        """
        publishes text onto configured platform/address
        """
        try:
            if self.connection.is_connected():
                self.connection.send(body=data,
                                     destination=self.config['transport'][
                                         'topic'])
        except Exception:
            self.logger.error(
                "could not send data to " + self.config['transport'][
                    'topic'] + ", reason unkown")
