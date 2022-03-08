






import threading
import time

from base.configReader import configuration
from infoExtraction.testInfoImageExtracton import testInfoImageExtracton
from preprocessor.testImagePreprocessor import testImagePreprocessor


publisher_config = configuration('preprocessor/testImagePreprocessorConfig.json')
publisher_config.load()

publisher = testImagePreprocessor(publisher_config)


subscriber_config = configuration('infoExtraction/testInfoImageExtractonConfig.json')
subscriber_config.load()

subscriber = testInfoImageExtracton(subscriber_config)

while(True):
    publisher.preprocess()
    time.sleep(20)



