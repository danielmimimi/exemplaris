import logging
import uuid

from typing import Any
from base.configReader import Configuration

from base.pubSubBase import PubSubBase


class Subscriber(PubSubBase):
    """Handles subscription with broker, sets callback function if topic is
    served """

    def __init__(self, config: Configuration, logger: logging):
        PubSubBase.__init__(self, config)
        self.config = config
        self.logger = logger
        self.connection.subscribe(destination=config['transport']['topic'],
                                  ack='auto', id=uuid.uuid4().hex)
        # self.logger.debug(
        # "subscribed to topic : "+config['transport']['topic'])

    def setListener(self, name: str, callbackFunction: Any):
        """Sets callback function"""
        self.connection.set_listener(name, callbackFunction)
        # self.logger.debug("set callback")
