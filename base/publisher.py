

import logging
from typing import Any
from base.configReader import configuration

from base.pubsubBase import pubsubBase


class publisher(pubsubBase):
    def __init__(self, config : configuration, logger : logging):
        pubsubBase.__init__(self,config)
        self.logger = logger

    def publish(self, data: Any):
        '''
        publishes saved data onto configured platform/adress
        '''
        try:
            if(self.connection.is_connected()):
                self.connection.send(body='something', destination=self.config['transport']['topic'])
        except Exception as ex:
            self.logger.error("could not send data to "+self.config['transport']['topic']+", reason unkown")

    