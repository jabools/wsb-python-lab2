from cv2 import imread, imwrite, imshow, waitKey, destroyAllWindows

from image_processor.manipulations.process import Process


class ImageProcessor:
    def __init__(self, image_path: str):
        self.__image_path = image_path
        self.__processSteps = list()
        self.__image = imread(image_path)

    def add_process(self, process: Process):
        self.__processSteps.append(process)

    def start(self, destination_path=None):
        image = self.__image

        for el in self.__processSteps:
            image = el.process(image)

        if destination_path is None:
            imwrite(self.__image_path, image)
        else:
            imwrite(destination_path, image)

        imshow('Original image', self.__image)
        imshow('Modified image', image)
        waitKey(0)
        destroyAllWindows()
