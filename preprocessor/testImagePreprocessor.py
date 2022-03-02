from base.configReader import configuration
from base.preprocessor import preprocessor

import cv2

class testImagePreprocessor(preprocessor):
    def __init__(self, config: configuration):
        super().__init__(config)

    def preprocess(self):
        capture = cv2.VideoCapture("tests\data\sample_1280x720_surfing_with_audio.mpeg")
        while(capture.isOpened()):
            (ret, imageMat) = capture.read()
            encodedSucess, encodedImage = cv2.imencode('.jpg',imageMat)
            self.publisher.publishImage(encodedImage)

        
