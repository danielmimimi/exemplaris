from base.configReader import configuration
from infoExtraction.testInfoExtracton import testInfoExtracton

import time

config = configuration('infoExtraction/testInfoExtractonConfig.json')
config.load()

prerocessor = testInfoExtracton(config)

while(True):
    time.sleep(10)