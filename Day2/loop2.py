x = ('HELLO', 'Hi', 20, 40.2, 9.6j, [1,2], 'PYTHON', 'JECRC', (1,2,3))
a = {}
for i in x:
    y = len(i)
    mid_in = y//2
    if y%2 == 0:
        a[i] = i[mid_in]
    elif y%2 != 0:
        fi = i[0]
        le = i[y-1]
        a[i] = fi+le

print(a)