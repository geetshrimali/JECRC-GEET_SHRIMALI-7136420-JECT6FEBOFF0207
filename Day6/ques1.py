
def add_nums(*args):
    #print(args, type(args))
    sum = 0
    for i in args:
        if type(i) in (int,float):
            sum += i
        else:
            continue
    print(f'addition:{sum}')

add_nums(1, 2, 'a', 'b', 4)


#double packing
def pr(**kwargs):
    print(kwargs)

pr(username = 'usr123', passw = '@@@')


#unpacking
def add_n(*args):
    #print(args, type(args))
    sum = 0
    for i in args:
        if type(i) in (int,float):
            sum += i
        else:
            continue
    print(f'addition:{sum}')

add_n(*eval(input('enter list of values: ')))
