import logging
from base.configReader import configuration

from base.publisher import publisher


class preprocessor:
    """the preprocessor is created via config file,
        it takes the data stream from the data-source and 
        applies preprocessing on it. At the end it will publish
        the data on configured endpoint."""
    def __init__(self, config : configuration):
        self.config = config.config
        self.logger = logging.basicConfig( level=logging.DEBUG, filename=self.config['name']+'.log')
        self.publisher = publisher(self.config,self.logger)

    def preprocess(self):
        '''
        reduces complexity of data or apply transformation.
        '''
        raise NotImplementedError()
