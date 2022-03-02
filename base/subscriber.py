import logging
import uuid

from typing import Any
from base.configReader import configuration

from base.pubsubBase import pubsubBase


class subscriber(pubsubBase):
    def __init__(self,  config : configuration, logger : logging):
        pubsubBase.__init__(self,config)
        self.config = config
        self.logger = logger
        self.connection.subscribe(destination=config['transport']['topic'],ack='auto',id=uuid.uuid4().hex)
        #self.logger.debug("subscribed to topic : "+config['transport']['topic'])

    def setListener(self,name:str, callbackFunction:Any):
        self.connection.set_listener(name, callbackFunction)
        #self.logger.debug("set callback")
        

    