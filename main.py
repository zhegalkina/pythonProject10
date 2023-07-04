class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_employee(self):
        print(name, salary)

display = Employee(input("Enter name "), input("Enter salary "))
