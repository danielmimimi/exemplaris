from base.configReader import Configuration
from base.preprocessor import Preprocessor


class TestPreprocessor(Preprocessor):
    def __init__(self, config: Configuration):
        super().__init__(config)

    def preprocess(self):
        self.publisher.publish('soeme')
