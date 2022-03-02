
import logging
import stomp
from base.configReader import configuration

from base.subscriber import subscriber


class infoExtractor():
    def __init__(self,config: configuration):
        self.config = config.config
        self.logger = logging.basicConfig(level=logging.DEBUG, filename=self.config['name']+'.log')
        self.subscriber = subscriber(self.config,self.logger)
        
