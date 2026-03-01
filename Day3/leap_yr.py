x = int(input())
if x%4 == 0:
    if x%100 == 0:
        if x%400 == 0:
            print('leap yr')
        else:
            print('not leap yr')
    else:
        print('Leap year')
else:
    print('not leap yr')