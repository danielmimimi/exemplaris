from base.configReader import configuration
from preprocessor.testPreprocessor import testPreprocessor

import time

config = configuration('preprocessor/testPreprocessorConfig.json')
config.load()

prerocessor = testPreprocessor(config)

while(True):
    prerocessor.preprocess()
    time.sleep(10)