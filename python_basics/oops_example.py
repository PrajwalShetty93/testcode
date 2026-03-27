

class Car:

    def __init__(self, brand, year):
        self.brand = brand
        self.year=year

    def get_age(self,current_year):
        return current_year-self.year


toyota=Car("Toyota", 2018)
print(toyota.brand)
print(toyota.year)
print(toyota.get_age(2026))    