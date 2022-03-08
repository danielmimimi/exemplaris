from base.configReader import configuration
from base.preprocessor import preprocessor

import cv2
import json
import subprocess

from utils.imageConverter import imageConverter

class splitAudioVideoPreprocessor(preprocessor):
    def __init__(self, config: configuration):
        super().__init__(config)

    def preprocess(self):
        converter = imageConverter()
        while(capture.isOpened()):
            (ret, imageMat) = capture.read()
            encodedImageJson = converter.imageEncode(imageMat)
            self.publisher.publish(json.dumps(encodedImageJson))
        capture.release()

    

    def convert_video_to_audio_ffmpeg(video_file, output_ext="mp3"):
        """Converts video to audio directly using `ffmpeg` command
        with the help of subprocess module"""
        filename, ext = os.path.splitext(video_file)
        subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"], 
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT)
        
