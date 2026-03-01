x = int(input('salary: '))
y = int(input('cibil score: '))
if x>25000 and y>700:
    if x > 50000 and y > 750:
        print('instantly approved')
    else:
        print('loan approval subject to bacckground verification')
else:
    print('not applicable for loan')
