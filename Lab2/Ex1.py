print('Enter a whole number between 1-100')
valueEntered = int(input())
# valEntered will take the users input and converts it to an integer

print('The value that you entered is', valueEntered) 
# Will return the number that the user entered

valueSquared = valueEntered ** 2
# valueSquared will hold the square of the number that the user entered

print('The square of the number is', valueSquared)
# Will return the square of the number that the user entered

print(f'The value that you entered is {valueEntered} and its square is {valueSquared}')