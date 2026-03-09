'''type of inheritance in which properties will be derived from single parent class to multiple child class'''

class Parent:
    gold = '2kg'
    silver = '10kg'
    no_of_flats = 12

class SmallBro(Parent):
    name = 'Rick'

class ElderBro(Parent):
    my_name = 'Rob'

class Sister(Parent):
    sis_name = 'Sansa'

print(SmallBro.gold)
print(ElderBro.silver)
print(Sister.no_of_flats)