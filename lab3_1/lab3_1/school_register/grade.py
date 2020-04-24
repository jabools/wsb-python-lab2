class Grade:
    def __init__(self, grade: int, weight: int):
        self.__grade = grade
        self.__weight = weight

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value: int):
        self.__grade = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value: int):
        self.__weight = value
