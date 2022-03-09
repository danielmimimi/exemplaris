import time

from base.configReader import Configuration
from infoExtraction.testInfoImageExtracton import TestInfoImageExtraction

if False:

    config = Configuration('infoExtraction/testInfoExtractonConfig.json')
    config.load()

    prerocessor = TestInfoImageExtraction(config)

else:
    config = Configuration('infoExtraction/testInfoImageExtractonConfig.json')
    config.load()

    prerocessor = TestInfoImageExtraction(config)

while True:
    time.sleep(10)
