class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_employee(self):
        print(self.name, self.salary)

display = Employee(input("Enter name: "), (input("Enter salary: ")))

display.display_employee()
