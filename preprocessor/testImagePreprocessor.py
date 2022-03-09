from base.configReader import Configuration
from base.preprocessor import Preprocessor

import cv2
import json

from utils.imageConverter import imageConverter


class TestImagePreprocessor(Preprocessor):
    def __init__(self, config: Configuration):
        super().__init__(config)

    def preprocess(self):
        capture = cv2.VideoCapture(
            "test\\data\\sample_1280x720_surfing_with_audio.mpeg")
        converter = imageConverter()
        while capture.isOpened():
            (ret, imageMat) = capture.read()
            encoded_image_json = converter.imageEncode(imageMat)
            self.publisher.publish(json.dumps(encoded_image_json))
        capture.release()
