import time

from base.configReader import Configuration
from infoExtraction.testInfoImageExtracton import TestInfoImageExtraction
from preprocessor.testImagePreprocessor import TestImagePreprocessor

publisher_config = Configuration(
    'preprocessor/testImagePreprocessorConfig.json')
publisher_config.load()

publisher = TestImagePreprocessor(publisher_config)

subscriber_config = Configuration(
    'infoExtraction/testInfoImageExtractonConfig.json')
subscriber_config.load()

subscriber = TestInfoImageExtraction(subscriber_config)

while True:
    publisher.preprocess()
    time.sleep(20)
