def factorial(a):                                       
    fa = 1
    for i in range(1,a+1):
        fa = fa*i
    print(fa)
factorial(a = int(input('Enter a number')))


import math as m 
x = int(input('Enter a number:'))
print('Square root:',m.sqrt(x))
print('Logarithm:',m.log(x))
print('Sine:',m.sin(x))
