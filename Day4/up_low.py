x = str(input())
if 97<=ord(x)<=122:
    y = ord(x)-32
    print(chr(y))
elif 65<=ord(x)<=90:
    y = ord(x)+32
    print(chr(y))
else:
    print((x))

