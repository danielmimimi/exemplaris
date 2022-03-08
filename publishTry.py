from base.configReader import configuration
from preprocessor.testPreprocessor import testPreprocessor
from preprocessor.testImagePreprocessor import testImagePreprocessor


import time


if False:
    config = configuration('preprocessor/testPreprocessorConfig.json')
    config.load()

    prerocessor = testPreprocessor(config)
if True:
    config = configuration('preprocessor/testImagePreprocessorConfig.json')
    config.load()

    prerocessor = testImagePreprocessor(config)

while(True):
    prerocessor.preprocess()
    time.sleep(20)