# Contains 3 functions: exponent, max, and min. Each function takes two numbers as input and returns the result of the respective operation.

def midpoint(num1, num2):
    return (num1 + num2) / 2

def squareroot(num):
    return num ** 0.5

def exponent(base, exp):
    return base ** exp

def max(num1, num2):
    return (num1 + num2 + abs(num1 - num2)) // 2

def min(num1, num2):
    return (num1 + num2 - abs(num1 - num2)) // 2