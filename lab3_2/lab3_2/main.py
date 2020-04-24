from image_processor import ImageProcessor
from image_processor.manipulations import Rotate, Grayscale


def main():
    processor = ImageProcessor('image.jpg')
    processor.add_process(Rotate(45))
    processor.add_process(Grayscale())
    processor.start('image-changed.jpg')


if __name__ == '__main__':
    main()
