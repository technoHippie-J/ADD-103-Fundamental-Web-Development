class Student:  # class names are capitalized
    def __init__(self, first_name, last_name, student_id, year):
        self.__last_name = last_name
        self.__student_id = student_id
        self.__year = year

    # method to get student's info as a formatted string
    def get_info(self):
        return f"{self.__first_name}{self.__last_name}, ID: {self.__student_id}, Year: {self.__year}"

    # Getter for first_name

    def get_first_name(self):
        return self.__first_name

    # Getter for last_name
    def get_last_name(self):
        return self.__last_name

    # Getter for studentID
    def get_studentID(self):
        return self.__studentID

    # Getter for year
    def get_year(self):
        return self.__year

    # Setter for first_name
    def set_first_name(self, first_name):
        self.__first_name = first_name

    # Setter for last_name
    def set_last_name(self, last_name):
        self.__last_name = last_name

    # Setter for studentID
    def set_studentID(self, studentID):
        self.__studentID = studentID

    # Setter for year
    def set_year(self, year):
        self.__year = year


def main():
    student_1 = Student("Meri", "Kasprak", "123456", "Super Senior")
    print(student_1.get_info())
    print(student_1.get_first_name(), student_1.get_last_name())
    student_1.set_last_name("Engel")
    print(student_1.get_info())
    # student_1.__last_name = "Summers" # doesn't work, but doesn't give error
    # print(student_1.get_info())

    student_2 = Student("Fred", "Flinstsont", "234566", "Freshman")
    print(student_2.get_info())
