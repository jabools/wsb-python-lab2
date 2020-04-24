from school_register import Register, Student, Grade, GradesCalculator


def main():
    class_a_register = Register()
    student1 = Student('Jan Kot', 12345678911)
    student2 = Student('Anna Nowak', 11987654321)

    class_a_register.add_student(student1)
    class_a_register.add_student(student2)

    class_a_register.add_grade(student1, Grade(3, 3))
    class_a_register.add_grade(student1, Grade(5, 2))
    class_a_register.add_grade(student1, Grade(2, 6))

    class_a_register.add_grade(student2, Grade(4, 1))
    class_a_register.add_grade(student2, Grade(2, 3))
    class_a_register.add_grade(student2, Grade(5, 4))

    grades_calculator = GradesCalculator(class_a_register)

    print("Student %s - grades average: %s" % (student1.name, grades_calculator.get_arithmetic_average(student1)))
    print("Student %s - grades average: %s" % (student2.name, grades_calculator.get_arithmetic_average(student2)))


if __name__ == '__main__':
    main()
