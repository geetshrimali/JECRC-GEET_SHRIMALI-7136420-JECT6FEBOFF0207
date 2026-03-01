char = eval(input('enter a character:'))
if ((char.type()) == int):
    print('digit')
elif (char.type() == str):
    if char in 'aeiouAEIOU':
        print('Vowel')
    else:
        if 