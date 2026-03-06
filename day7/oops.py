
#Object Oriented Programming System (OOPS)
'''
type of programming where we only se class and object
'''

#Advantages
'''
Code Reusability
Multi tasking
Data Security
Data hiding
for better code organisation
Better readability

For developing real-world applications or solving real world problems, we prefer to use oops.
'''

#class
'''
it is a blueprint of an object in which all the properties and unctionalities will bw stored.
'''

#object
'''
The outcome of a class or instance of a class
'''

#To create a class we have to use aa keyword called 'class'
'''
class 'classname':
    properties(variables)
    functionalities(methods)

obj_name = classname(args)
'''

#class Car:
    #wheels = 4
    #engine = 'petrol'
   # base_speed = '40kmph'
   # max_speed = '120kmph'
  #  gears = 4

#print(Ferrari)  #print memory address
#BMW = Car()

#print(f'ENgine Type: {BMW.engine}')
#print(f'max speed: {BMW.max_speed}')
#print(f'base speed: {BMW.base_speed}')
#print(f'gears: {BMW.gears}')

#properties/states/members
'''
properties are variables which we can create inside class or object

exactly 2 properties:

1)class proprties
2)Object properties

variables inside a class will be known as properties of a class

for every object, class members will be same
'''

#BMW.air_bags = True
#BMW.adas = True
#print(f'airbags: {BMW.air_bags}')

#constructor (__init__)
'''
class 'classname':
    properties
    
    def __init__(self, arg1, arg2, arg3, arg4,..., argn):
        self.arg1 = arg1
        self.arg2 = arg2
        ...
        self.argn = argn
'''

class Car:
    wheels = 4
    engine = 'petrol'
    base_speed = '40kmph'
    max_speed = '120kmph'
    gears = 4
    def __init__(self, air_bags, security, base_budget, variant, total_sale):
        self.air_bags = air_bags
        self.base_budget = base_budget
        self.security = security
        self.variant = variant
        self.total_sale = total_sale

Ferrari = Car(True, '2Cr', 'level 7', 'base','20')

    #constructor
'''
    __init__ known as constructor
    used to initialize properties of an object
    dont have to call init explicitly. automatically invoke during object creation
    using __init__, use self as first argument
    'self' will refer to current execution context
    if we want, we can use any variable name in place of 'self', but self is preferred
'''

    #Methods
'''
object
calss
static

1) object method:
    used to modify properties of object

        class 'classname':
            def method_name(self, args):
                Statements
                Blocks
'''




'''
2)Class Method:
used to modify properties of class
@classmethod decorator is required to create one class method

       class 'classname':
        @classmethod
        def method_name(cls , args):
            Statements
            Blocks
'''