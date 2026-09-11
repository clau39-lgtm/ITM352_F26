# Imports the HandyMath module to use its functions.
import HandyMath

# Prompts the user to enter two numbers and stores them in variables num1 and num2.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calls the functions from the HandyMath module to perform various calculations and prints the results.
print(f"The midpoint between {num1} and {num2} is: {HandyMath.midpoint(num1, num2)}")
print(f"The square root of {num1} is: {HandyMath.squareroot(num1)}")
print(f"The result of {num1} raised to the power of {num2} is: {HandyMath.exponent(num1, num2)}")
print(f"The maximum of {num1} and {num2} is: {HandyMath.max(num1, num2)}")
print(f"The minimum of {num1} and {num2} is: {HandyMath.min(num1, num2)}")