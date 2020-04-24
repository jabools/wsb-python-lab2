from image_processor.manipulations.process import Process
from cv2 import getRotationMatrix2D, warpAffine


class Rotate(Process):
    def __init__(self, degrees: int):
        self.__degrees = degrees

    def process(self, image):
        (height, width) = image.shape[:2]

        center = (width / 2, height / 2)
        matrix = getRotationMatrix2D(center, self.__degrees, 1.0)
        return warpAffine(image, matrix, (width, height))
