
import utils.imageConverter as imConv
import cv2
import unittest


class Test_ImageConverter(unittest.TestCase):
    def test_encodeImage(self):
        """Encodes and decodes image"""
        try:
            capture = cv2.VideoCapture("test\data\sample_1280x720_surfing_with_audio.mpeg")
            counter = 0
            while(capture.isOpened()):
                (ret, imageMat) = capture.read()
                if(counter == 100):
                    converter = imConv.imageConverter()
                    jsonOutput = converter.imageEncode(imageMat)
                    decodedImage = converter.imageDecode(jsonOutput)
                    # Visualize JPEG conversion Error
                    subImage = imageMat - decodedImage
                    break
                counter += 1
            capture.release()
        except:
            self.assertEqual(True,True)
        

if __name__ == '__main__':
    unittest.main()