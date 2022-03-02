import stomp
import numpy as np
import cv2
from base.configReader import configuration
from base.infoExtractor import infoExtractor

class testInfoImageExtracton(infoExtractor,stomp.ConnectionListener):
    """test to visualize concept"""
    def __init__(self, config: configuration):
        super().__init__(config)
        self.subscriber.setListener(self.config['name'],self)

    def on_error(self, headers):
        """callback when topic receives an error"""
        print(headers)

    def on_message(self, headers):
        """callback when topic receives data"""
        nparr = np.fromstring(headers.body, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # cv2.IMREAD_COLOR in OpenCV 3.1

        print(headers.body)

