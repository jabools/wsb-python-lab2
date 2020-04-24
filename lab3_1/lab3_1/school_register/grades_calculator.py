from school_register.student import Student
from school_register.register import Register


class GradesCalculator:
    def __init__(self, register: Register):
        self.__register = register

    def get_arithmetic_average(self, student: Student):
        student_grades = self.__register.get_student_grades(student)

        grades_sum = 0
        weights_sum = 0

        for el in student_grades:
            grades_sum += el.grade * el.weight
            weights_sum += el.weight

        return round(grades_sum / weights_sum, 2)
