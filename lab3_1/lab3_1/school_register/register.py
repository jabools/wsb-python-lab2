from school_register.student import Student
from school_register.grade import Grade
from school_register.register_validator import RegisterValidator


class Register:
    def __init__(self):
        self.__studentsGradesDict = {}
        self.__validator = RegisterValidator(self.__studentsGradesDict)

    def add_student(self, student: Student):
        self.__validator.check_if_students_exists(student)
        self.__studentsGradesDict[student.pesel] = list()

    def add_grade(self, student: Student, grade: Grade):
        self.__validator.check_if_students_does_not_exist(student)
        self.__studentsGradesDict[student.pesel].append(grade)

    def get_student_grades(self, student: Student):
        self.__validator.check_if_students_does_not_exist(student)
        return self.__studentsGradesDict[student.pesel]
