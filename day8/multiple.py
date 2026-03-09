'''it is a type of inheritance in which the propeties wwill be derived from multiple parent classes to a single child class'''

class Parent1:
    a = 'class_1'

class Parent2:
    b = 'class_2'

class Parent3:
    c = 'class_3'

class Parent4:
    d = 'class_4'

class Child(Parent1, Parent2, Parent3, Parent4):
    pass

print(Child.a, Child.b, Child.c, Child.d)
