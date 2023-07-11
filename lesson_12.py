class Passport:
    def __init__(self, name, surname, date, country,number):
        self.name = name
        self.surname = surname
        self.date = date
        self.country = country
        self.number = number
    def PrintInfo(self):
        print(f"Name and Surname: {self.name} {self.surname}")
        print(f"Date: {self.date}")
        print(f"Country: {self.country}")
        print(f"Number: {self.number}")

# passports = Passport('Tanya', 'Z', 17_05, 'Rus', '111')
# passports.PrintInfo()

class ForeignPassport(Passport):
    def __init__(self, name, surname, date, country, number, visa):
        super().__init__(name, surname, date, country, number)
        self.visa = visa
    def PrintInfo(self):
        super().PrintInfo()
        print(f"Visa: {self.visa}")

passports_foreign = ForeignPassport('Tanya', 'Z', 17_05, 'Rus', '111', 'Egypt')
passports_foreign.PrintInfo()


