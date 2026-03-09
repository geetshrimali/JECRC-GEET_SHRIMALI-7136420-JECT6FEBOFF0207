#multi-level
'''type of inheritance where properties derived from one to another by considering more than one level'''

class Class1:
    a = 'class_1'

class Class2(Class1):
    b = 'class_2'

class Class3(Class2):
    c = 'class_3'

class Class4(Class3):
    d = 'class_4'

class Class5(Class4):
    e = 'class_5'

obj = Class5()
print(obj.a, obj.b, obj.c, obj.d, obj.e)