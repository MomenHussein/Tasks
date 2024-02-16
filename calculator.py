import math as m


def factorial(number):
    if number == 1:
        return 1
    else:
        return number*factorial(number-1)

def modulus(number):
    number = int(input("Enter number: "))
    if number >=0:
        return number
    return (-1 * number)

def power(number,power):
    number = int(input("Enter number: "))
    power = int(input("Enter power: "))
    multiply = 1
    i = 0
    while i < power:
        multiply*= number
        i+=1
    return multiply

def square(number):
    number = int(input("Enter number: "))
    multiply = 1
    for i in range(2):
        multiply*=number
    return multiply

def nthroot(number,root):
    number = int(input("Enter number: "))
    root = int(input("Enter root: "))
    return m.power(number,(1/root))

def square_root(number):
    number = int(input("Enter number: "))
    return m.sqrt(number)

def cos(number):
    number = int(input("Enter number: "))
    return m.cos(number)

def sin(number):
    number = int(input("Enter number: "))
    return m.sin(number)

def tan(number):
    number = int(input("Enter number: "))
    return m.tan(number)

def cosh(number):
    number = int(input("Enter number: "))
    return m.cosh(number)

def sinh(number):
    number = int(input("Enter number: "))
    return m.sinh(number)

def tanh(number):
    number = int(input("Enter number: "))
    return m.tanh(number)

def multiplicity(num1,num2):
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    return num1*num2

def multiplicity_reverse(number):
    number = int(input("Enter number: "))
    return 1/number

def division(num1,num2):
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    return num1/num2

def addition(num1,num2):
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    return num1+num2

def substraction(num1,num2):
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    return num1-num2

def precentage(number,total):
    number = int(input("Enter number: "))
    total = int(input("Enter total: "))
    return (number/total)*100

def remaining(num1,num2):
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    return num1//num2

def exponential():
    return m.e

def exponential1(number):
    number = int(input("Enter number: "))
    return m.exp(number)

def degree(number):
    number = int(input("Enter number: "))
    return m.degrees(number)

def mod(num1,num2):
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    return m.fmod(num1, num2)

def acos(number):
    number = int(input("Enter number: "))
    return m.acos(number)

def asin(number):
    number = int(input("Enter number: "))
    return m.asin(number)

def atan(number):
    number = int(input("Enter number: "))
    return m.atan(number)

def acosh(number):
    number = int(input("Enter number: "))
    return m.acosh(number)

def asinh(number):
    number = int(input("Enter number: "))
    return m.asinh(number)

def atanh(number):
    number = int(input("Enter number: "))
    return m.atanh(number)

def log(number,base):
    number = int(input("Enter number: "))
    base = int(input("Enter base: "))
    return m.log(number,base)

def log10(number):
    number = int(input("Enter number: "))
    return m.log10(number)

def ln(number):
    number = int(input("Enter number: "))
    return m.log(number,m.e)

def calculation(sign, num1, num2, number):
    loop = True
    while loop:
        sign = input("Enter operation: ").lower()
        if (sign == '+' or sign == 'addition' or sign == 'adding'):
            print(addition(num1, num2))
        elif (sign == '*' or sign == 'multiplicity' or sign == 'multilplication'):
            print(multiplicity(num1, num2))
        elif (sign == '%' or sign == 'precentage'):
            print(precentage(num1, num2))
        elif (sign == '^' or sign == 'power'):
            print(power(num1,num2))
        elif (sign == '/' or sign == 'division' or sign == 'divising'):
            print(division(num1, num2))
        elif (sign == '-' or sign == 'sunbstracting' or sign == 'substraction'):
            print(substraction(num1, num2))
        elif (sign == '//' or sign == 'remaining'):
            print(remaining(num1, num2))
        elif (sign == 'mod'):
            print(mod(num1, num2))
        elif (sign == 'log10' or sign == 'logbase10'):
            print(log(num1,num2))
        elif (sign == '!' or sign == 'factorial' or sign == 'factoralization'):
            number = int(input("Enter number: "))
            print(factorial(number))
        elif (sign =='mod'):
            print(mod(number))
        elif(sign == 'modulus' or sign == '\\' ):
            print(modulus(number))
        elif (sign == 'square'):
            print(square(number))
        elif (sign =='square_root' or sign =='square root'):
            print(square_root(number))
        elif (sign =='cos' or sign =='cosin'):
            print(cos(number))
        elif (sign=='sin'):
            print(sin(number))
        elif (sign =='tan'):
            print(tan(number))
        elif (sign == 'cosh'):
            print(cosh(number))
        elif (sign == 'sinh'):
            print(sinh(number))
        elif (sign == 'tanh'):
            print(tanh(number))
        elif (sign == 'e' or sign == 'exp' or sign == 'exponential'):
            print(exponential())
        elif (sign == 'multiplicity_reverse' or sign =='multiplicityreverse'):
            print(multiplicity_reverse(number))
        elif (sign == 'multi exp'):
            print(exponential1(number))
        elif (sign == 'deg' or sign == 'degree'):
            print(degree(number))
        elif (sign == 'acos' or sign == 'acosin'):
            print(acos(number))
        elif (sign == 'asin'):
            print(asin(number))
        elif (sign == 'atan'):
            print(atan(number))
        elif (sign == 'acosh' or sign == 'acoshin'):
            print(acosh(number))
        elif (sign == 'asinh'):
            print(asinh(number))
        elif (sign == 'atanh'):
            print(atanh(number))
        elif (sign == 'log'):
            print(log10(number))
        elif (sign == 'ln'):
            print(ln(number))
        elif (sign == 'nthroot' or sign =='n_root'):
            print(nthroot(num1,num2))
        else:
            print("Sorry invalid operation")
            break

sign = ''
num1, num2, number = 0, 0, 0
calculation(sign, num1, num2, number)
    
        