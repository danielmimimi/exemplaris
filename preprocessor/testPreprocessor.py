from base.configReader import configuration
from base.preprocessor import preprocessor

class testPreprocessor(preprocessor):
    def __init__(self, config: configuration):
        super().__init__(config)

    def preprocess(self):
        self.publisher.publishText('soeme')
