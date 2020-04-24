class Student:
    def __init__(self, name: str, pesel: int):
        self.__name = name
        self.__pesel = pesel

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def pesel(self):
        return self.__pesel

    @pesel.setter
    def pesel(self, value: int):
        self.__pesel = value
