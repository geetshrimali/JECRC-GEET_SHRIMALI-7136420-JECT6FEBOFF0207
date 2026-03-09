#inheritance
'''
single level
multi level
multiple
hierarchial
hybrid
'''

#single level


                                            # class Parent:
                                            #     bank_balance = '54L'
                                            #     def desc(self):
                                            #         print('i am parent class')

                                            # class Child(Parent):
                                            #     pass

                                            # obj = Child()
                                            # print(obj.bank_balance)
                                            # obj.desc()



#constructor chaining
'''
Calling parent class's constructor from inside cchild class constructor is known as constructor chaining'''

                                            # class Parent:
                                            #     bank_balance = '54L'
                                            #     def __init__(self, members):
                                            #         self.members = members
                                            #     def desc(self):
                                            #         print('i am parent class')

                                            # class Child(Parent):
                                            #     def __init__(self, *args):
                                            #         super().__init__(args)

                                            # obj = Child('Mom', 'Dad')
                                            # print(obj.members)




                                            # class Parent:
                                            #     bank_balance = '54L'
                                            #     def __init__(self, members):
                                            #         self.members = members
                                            #     def desc(self):
                                            #         print('i am parent class')

                                            # class Child(Parent):
                                            #     def __init__(self, child_name, *args):
                                            #         self.child_name = child_name
                                            #         super().__init__(args)

                                            # obj = Child('hehe', 'Mom', 'Dad')
                                            # print(obj.members)
                                            # print(obj.child_name)


class Parent:
    bank_balance = '54L'
    def __init__(self, members):
        self.members = members
    def desc(self):
        print('i am parent class')

class Child(Parent):
    def __init__(self, child_name, *args):
        self.child_name = child_name
        super().__init__(args)

    def display(self):
        super().desc()

obj = Child('hehe', 'Mom', 'Dad')
print(obj.members)
print(obj.child_name)
obj.display()