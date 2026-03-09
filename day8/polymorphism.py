'''using same method name or operator to perform two or more different operations'''

                                                    # class Temp:

                                                    #     def sum(self, a, b):
                                                    #         print(a + b)

                                                    #     def sum(self, a, b, c):
                                                    #         print(a+b+c)

                                                    # obj = Temp()
                                                    # obj.sum(10, 20)
                                                    # #obj.sum(10, 20, 30)


'''in python if we havee to perform methd overloading, then it will act as method overwriting, in other prog languages, based upon no of arguments
the respective method block will get executed. but in python it never happens'''

'''method overriding is a phenomenon of overriding the prev mwthod's address with latest one'''


#monkey patching
'''it is a process of storing prev method's address inside a variable before overriding the method area's address. Using that var, we can access the
prev method's method area'''
                                                    # class Temp:

                                                    #     def sum(self, a, b):
                                                    #         print(a + b)

                                                    #     add_two_sum = sum

                                                    #     def sum(self, a, b, c):
                                                    #         print(a+b+c)

                                                    # obj = Temp()
                                                    # obj.add_two_sum(10, 20)
                                                    # obj.sum(10, 10, 10)
                                                    # #obj.sum(10, 20, 30)



class new():
    def __init__(self, val):
        self.val = val

    def __add__(self, an_object):
        return self.val + an_object.val

obj1 = new(10)
obj2 = new(20)
print(10 + 20)
print(obj1 + obj2)
