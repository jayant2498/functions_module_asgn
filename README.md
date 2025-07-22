# functions_module_asgn

def factorial(a):                                                                   # created a function named factorial and passed a as the argument
    if a==0:                                                                        # if a is 0 the factorial is 1 
        print(1,'is factorial')
    elif a<0:                                                                       # if a is less than 0 the factorial is undefined
        print('Undefined')
    else :                                                                          # calculates the fact
        fa = 1                                                                      # fa = 1 variable is assigned = 1 
        for i in range(1,a+1):                                                      # iterates till the number entered by the user
            fa = fa*i
        print(fa)                                                                   # returns factorial
factorial(a = int(input('Enter a number')))                                         # Taking inputs from the user



import math as m                                                                    # import math module as m 
x = int(input('Enter a number:'))                                                   # taking integer input from the user.
print('Square root:',m.sqrt(x))                                                     
print('Logarithm:',m.log(x))
print('Sine:',m.sin(x))
