tallies = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
tallies_reverse = {"M":1000, "D": 500, "C":100, "L": 50, "X":10, "V": 5, "IV": 4, "I": 1}

class Transformer:
    def __init__(self, tallies):
        self.tallies = tallies
    def roman_to_decimal(roman_number="XXIV"):
        sum = 0
        for i in range(len(roman_number)-1):
            left = roman_number[i]
            right = roman_number[i+1]
            if tallies[left] < tallies[right]:
                sum-=tallies[left]
            else:
                sum+=tallies[left]
        sum +=tallies[roman_number[-1]]
        return sum
    print("XXIV=", roman_to_decimal())



    def decimal_to_roman(number):
        roman = ''
        for letter, value in tallies_reverse.items():
            while number >= value:
                roman += letter
                number -= value
        return roman
    print("3014 =", decimal_to_roman(3014))