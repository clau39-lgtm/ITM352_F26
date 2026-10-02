# First version of the quiz game
# Name: Coleman Lau
# Date: October 2, 2026

answer = input("What is the capital of France? ")
if answer == "Paris" or answer == "paris":
    print("Correct!")
else:
    print(f"Incorrect! The correct answer is Paris not {answer!r}")

answer = input("What is the capital of Germany? ")
if answer == "Berlin" or answer == "berlin":
    print("Correct!")
else:
    print(f"Incorrect! The correct answer is Berlin not {answer!r}")