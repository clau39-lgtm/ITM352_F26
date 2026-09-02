# This program prompts the user to enter a decimal number between 1-100, calculates the square of that number,
# rounds it to two decimal places, and then prints both the entered number and its square.
# Name: Coleman Lau
# Date: 9/2/2026

valueEntered = float(input('Enter a decimal number between 1-100: '))
# valueEntered will take the users input and converts it to a float

print('The value that you entered is', valueEntered) 
# Will return the number that the user entered

valueSquared = valueEntered ** 2
# valueSquared will hold the square of the number that the user entered

rounded_value = round(valueSquared, 2)

print('The square of the number is', rounded_value)
# Will return the square of the number that the user entered)

print(f'The value that you entered is {valueEntered} and its square is {rounded_value}')