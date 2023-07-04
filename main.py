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
    def __init__(self, legs, tail, domestic, mammals):
        self.legs = legs
        self.tail = tail
        self.domestic = domestic
        self.mammals = mammals
    def is_animals(self):
        if self.mammals == True:
            print("mammals")
        else:
            print("not mammals")

    def is_domestic(self):
        if self.domestic == True:
            print("domestic")
        else:
            print("not domestic")

example = Animal(4, True, True, True)
example.is_animals()
example.is_domestic()








