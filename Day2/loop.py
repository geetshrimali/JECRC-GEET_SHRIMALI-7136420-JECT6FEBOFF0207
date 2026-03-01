x = str(input('enter string: '))
y = ""
for letter in x:
    if 97 <= ord(letter) <= 122:          
        y += chr(ord(letter) - 32)
    elif 65 <= ord(letter) <= 90:          
        y += chr(ord(letter) + 32)
    else:
        y += letter                  

print(y)
