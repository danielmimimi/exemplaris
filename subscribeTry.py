import time

from base.configReader import configuration
from infoExtraction.testInfoExtracton import testInfoExtracton
from infoExtraction.testInfoImageExtracton import testInfoImageExtracton

if False:

    config = configuration('infoExtraction/testInfoExtractonConfig.json')
    config.load()

    prerocessor = testInfoExtracton(config)

else:
    config = configuration('infoExtraction/testInfoImageExtractonConfig.json')
    config.load()

    prerocessor = testInfoImageExtracton(config)

while(True):
    time.sleep(10)