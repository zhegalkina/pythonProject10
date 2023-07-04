# class Employee:
#
#     emp_count = 0
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.emp_count += 1
#     def display_employee(self):
#         print("Name:", self.name, "salary", self.salary)
#
#     def display_count(self):
#         print("All", Employee.emp_count)
#
# emp = Employee("Tom", 5000)
#
# emp.display_employee()
# emp.display_count()
# emp2 = Employee("Anton", 4000)
# emp2.display_count()


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
# class Freelance(Employee):
#     def __init__(self, name, salary, email):
#         super().__init__(name, salary)
#         self.email = email
#     def display_email(self):
#         print("Name:", self.name, "salary", self.salary, "email", self.email)
#
# example = Freelance("Tom", 5000, "email")
# example.display_email()


class Animal:
    def __init__(self):
        self.legs = 4
        self.tail = True
        self.domestic = True
        self.mammals = True
    def is_animals(self):
        if self.mammals:
            print("mammals")


    def is_domestic(self):
        if self.domestic :
            print("domestic")


class Dogs(Animal):
    def __init__(self):
        super().__init__()
    def is_mammal(self):
        super().is_mammal()

Tom = Dogs()
Tom.is_mammal()










