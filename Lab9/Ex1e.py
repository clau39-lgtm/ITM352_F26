# Read the entire file using readlines()

with open("names.txt", "r") as file_object:  # Open the file in read mode using 'with'
    names = file_object.readlines()  # Read all lines into a list
    print(f"Number of names: {len(names)}")  # Print the number of names in the file
    for name in names:
        print(name.strip())  # Print each name without leading/trailing whitespace