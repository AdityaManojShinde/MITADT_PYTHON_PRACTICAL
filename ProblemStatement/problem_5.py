# Problem Statement
# Create a Student class to represent a student. Use private attributes for the student’s:

# Name
# Roll number
# Grades
# Provide getter and setter methods to access and modify these private attributes.

class Student:
    def __init__(self,name,roll,grades):
        self.__name = name
        self.__roll = roll
        self.__grades = grades
    def get_name(self):
        return self.__name
    def get_roll(self):
        return self.__roll
    def get_grades(self):
        return self.__grades
    def set_name(self,name):
        self.__name = name
    def set_roll(self,roll):
        self.__roll = roll
    def set_grades(self,grades):
        self.__grades = grades

student1 = Student("Aditya", 57, [85, 90, 95])

# This will cause error => AttributeError: 'Student' object has no attribute '__name'
# print(student1.__name)
# print(student1.__roll)
# print(student1.__grades)

# Test the getter and setter methods
print(student1.get_name()) # Output: Aditya
print(student1.get_roll()) # Output: 57
print(student1.get_grades()) # Output: [85, 90, 95]
student1.set_name("Aditya Shinde")
print(student1.get_name()) # Output: Aditya Shinde
