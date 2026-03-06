'''
(str)
lower
upper
capitalize
title
strip
lstrip
rstrip
replace
index
split
join
startswith
endswith
isdigit
isalpha
islower
isupper'''

x = 'ABCDE'
print(x.strip('E'))
print(x.lstrip('A'))
print(x.strip('E'))
print(x.index('E'))
print(x.replace('E', 'G'))

y = 'python programming'
z = y.split()
print(z)
print(' '.join(z))

'''
(list)
append
insert
extend
pop
remove
clear
sort
reverse
index
count
'''

list = [1, 7 , 5,10, 6, 99, 57]
print(list)

list.sort()
print(list)

list.sort(reverse = True)
print(list)

print(list.index(6))

print(list.count(99))


'''
(tuple)
index
count
'''

tuple = (1, 2, 3, 3 ,4)
print(tuple.index(2))
print(tuple.count(3))

'''
(set)
add
remove
discard
pop
clear
union
intersection
diffference
symmetric_difference
'''
set = {1, 2, 3, 4}

set_2 = {5, 6, 3, 4}
s3 = set.union(set_2)
print(s3)

s4 = set.intersection(set_2)
print(s4)

set.add(5)
print(set)

set.add((1,2,3))

set.remove(5)
print(set)

set.discard(9)
print(set)

'''
(dictionary)
get()
pop()
popitem()
clear()
keys
values
'''
dict = {1:4, 2:2, (1, 2, 3): (1,2,3)}
print(dict)
print(dict.get(2))
print(dict[1])

dict.pop(1)
print(dict)

dict.popitem()
print(dict)

dict[2] = '123'
print(dict)

dict.update({2:1414})
print(dict)

print(dict.keys())
print(dict.values())


#packing
def add_nums(*args):
    print(args, type(args))
    sum = 0
    for i in args:
        sum += i
    print(f'addition:{sum}')

add_nums(1, 2, 3, 4, 5, 5, 6)