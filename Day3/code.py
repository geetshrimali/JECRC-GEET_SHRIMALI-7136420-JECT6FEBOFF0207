a = str(input('enter username: '))
x = 'user123'
y = 1234

if a == x:
    b = (input('enter password: '))
    if int(y) == b:
        print('login successfull')
    else:
        print('wrong password')
else:
    print("wrong username")            