from school_register.student import Student


class RegisterValidator:
    def __init__(self, dictionary: dict):
        self.__dictionary = dictionary

    def check_if_students_exists(self, student: Student):
        if student.pesel in self.__dictionary:
            raise Exception("Student with the same PESEL already exists in this register.")

    def check_if_students_does_not_exist(self, student: Student):
        if student.pesel not in self.__dictionary:
            raise Exception("Given student does not belong to this register.")
