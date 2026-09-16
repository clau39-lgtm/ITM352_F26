first = input("Enter the first name: ")
middle_initial = input("Enter the middle initial: ")
last = input("Enter the last name: ")

full_name = first + " " + middle_initial + ". " + last
print("Your full name is:", full_name)

print(f"Your full name using f-string is: {first} {middle_initial}. {last}")
print("Your full name using " + "%" + " formatting is: %s %s. %s" % (first, middle_initial, last))
print("Your full name using format method is: {} {}. {}".format(first, middle_initial, last))
print("Your full name using join method is: " + " ".join([first, middle_initial + ".", last]))