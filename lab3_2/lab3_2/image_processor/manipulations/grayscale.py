from image_processor.manipulations.process import Process
from cv2 import cvtColor, COLOR_BGR2GRAY


class Grayscale(Process):
    def process(self, image):
        return cvtColor(image, COLOR_BGR2GRAY)
