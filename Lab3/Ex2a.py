# This program prompts the user to enter two numbers and will return the midpoint between them.
# Name: Coleman Lau
# Date: 9/9/2026

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Function to calculate the midpoint between two numbers
def midpoint(num1, num2):
    return (num1 + num2) / 2

print(midpoint(num1, num2))  # Output: midpoint between num1 and num2