x = int(input())
if (0<=x<=100):
    y = x*5  
elif (100<x<=300):
    y = (500+(x-100)*7)  
elif (300<x):
    y = (500+1400+(x-300)*10)   
else:
    print('invalid')
    exit()


if(y > 5000):
    y = (y*.95)

print(y)