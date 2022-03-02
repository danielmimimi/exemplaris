

import logging
from typing import Any
from base.configReader import configuration

from base.pubsubBase import pubsubBase


class publisher(pubsubBase):
    '''
    Handles the publishing of different kind of data
    '''
    def __init__(self, config : configuration, logger : logging):
        pubsubBase.__init__(self,config)
        self.logger = logger

    def publishText(self, data: str):
        '''
        publishes text onto configured platform/adress
        '''
        try:
            if(self.connection.is_connected()):
                self.connection.send(body=data, destination=self.config['transport']['topic'])
        except Exception as ex:
            self.logger.error("could not send data to "+self.config['transport']['topic']+", reason unkown")

    def publishImage(self, data: Any):
        '''
        publishes image onto configured platform/adress
        '''
        try:
            if(self.connection.is_connected()):
                self.connection.send(body=data.tostring(), destination=self.config['transport']['topic'])
        except Exception as ex:
            self.logger.error("could not send data to "+self.config['transport']['topic']+", reason unkown")

    