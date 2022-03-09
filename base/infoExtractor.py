import logging
from base.configReader import Configuration

from base.subscriber import Subscriber


class InfoExtractor:
    """Base class for information extraction"""

    def __init__(self, config: Configuration):
        self.config = config.config
        # TODO figure out if logging requires an instance to be held
        logging.basicConfig(
            level=logging.DEBUG, filename=config.config['name'] + '.log')
        self.subscriber = Subscriber(self.config, None)  # FIXME
