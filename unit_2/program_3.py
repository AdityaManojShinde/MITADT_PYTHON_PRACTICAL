# Inheritence
class Person:
    def __init__(self, name , age):
        self.name = name 
        self.age = age

    def display_info(self):
        print(f"\nName: {self.name}\nAge : {self.age} years")

class Employee(Person):
    def __init__(self, name, age, id, salary):
        super().__init__(name,age)
        self.id = id
        self.salary = salary
    def display_employee_info(self):
        self.display_info()
        print(f"ID : {self.id}")
        print(f"Salary : {self.salary} $")

class Manager(Employee):
    def __init__(self, name, age, id, salary, department):
        super().__init__(name, age, id, salary)
        self.department = department
    def display_manager_info(self):
        self.display_employee_info()
        print(f"Department : {self.department}")


manager = Manager(name="Aditya Shinde",age=20,id="ADTSOCB1703",salary=100000,department="IT")
manager.display_employee_info()
manager.display_manager_info()