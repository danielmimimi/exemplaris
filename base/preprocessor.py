import logging
from base.configReader import Configuration

from base.publisher import Publisher


class Preprocessor:
    """the Preprocessor is created via config file,
        it takes the data stream from the data-source and
        applies preprocessing on it. At the end it will publish
        the data on configured endpoint."""

    def __init__(self, config: Configuration):
        self.config = config.config
        # todo figure out if a logging instance needs to be kept in some way
        logging.basicConfig(level=logging.DEBUG,
                            filename=self.config['name'] + '.log')
        self.publisher = Publisher(self.config, None)  # FIXME 2nd arg

    def preprocess(self):
        '''
        reduces complexity of data or apply transformation.
        '''
        raise NotImplementedError()
