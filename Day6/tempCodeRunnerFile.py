#create a function that returns list of prime num. please make sure that user can pass n inputs. for checking wether num is prime or not, you can create a fun.

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True
         
def prime_re(*args):
    prime = []
    for num in args:
        if isPrime(num):
            prime.append(num)
    return prime

print(prime_re(*eval(input('enter number/s: '))))

