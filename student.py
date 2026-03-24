class Student:
    def __init__(self, roll, name, course, marks, attendance):
        self.__roll = roll
        self.__name = name
        self.__course = course
        self.__marks = marks
        self.__attendance = attendance

    # Getters
    def get_roll(self):
        return self.__roll

    def get_name(self):
        return self.__name

    def get_course(self):
        return self.__course

    def get_marks(self):
        return self.__marks

    def get_attendance(self):
        return self.__attendance

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_course(self, course):
        self.__course = course