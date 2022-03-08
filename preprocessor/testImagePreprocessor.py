from base.configReader import configuration
from base.preprocessor import preprocessor

import cv2
import json

from utils.imageConverter import imageConverter

class testImagePreprocessor(preprocessor):
    def __init__(self, config: configuration):
        super().__init__(config)

    def preprocess(self):
        capture = cv2.VideoCapture("test\data\sample_1280x720_surfing_with_audio.mpeg")
        converter = imageConverter()
        while(capture.isOpened()):
            (ret, imageMat) = capture.read()
            encodedImageJson = converter.imageEncode(imageMat)
            self.publisher.publish(json.dumps(encodedImageJson))
        capture.release()


        
