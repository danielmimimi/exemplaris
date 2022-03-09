import json
import cv2
import numpy as np
import base64


class imageConverter:
    """Serializes and Deserializes single frames"""

    def __init__(self) -> None:
        pass

    def imageEncode(self, image):
        """encodes cv mat"""
        data = {}
        encodeSuccess, buffer = cv2.imencode('.jpg', image)
        if (encodeSuccess):
            data['size'] = image.shape[0:2]
            data['channels'] = image.shape[2]
            data['image'] = base64.b64encode(buffer).decode()
        return data

    def imageDecode(self, data: json):
        """decodes byte stream"""
        jpg_original = base64.b64decode(data['image'])
        jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
        image_64_decode = cv2.imdecode(jpg_as_np, flags=cv2.IMREAD_COLOR)
        return image_64_decode
