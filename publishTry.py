from base.configReader import Configuration
from preprocessor.testPreprocessor import TestPreprocessor
from preprocessor.testImagePreprocessor import TestImagePreprocessor

import time

if False:
    config = Configuration('Preprocessor/testPreprocessorConfig.json')
    config.load()

    preprocessor = TestPreprocessor(config)
if True:
    config = Configuration('preprocessor/testImagePreprocessorConfig.json')
    config.load()

    preprocessor = TestImagePreprocessor(config)

while True:
    preprocessor.preprocess()
    time.sleep(20)
