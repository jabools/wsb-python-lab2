from abc import ABC, abstractmethod


class Process(ABC):
    @abstractmethod
    def process(self, image):
        pass
