# Open a file using "with"

with open("names.txt", "r") as file_object:  # Open the file in read mode using 'with'
    print(type(file_object))  # Print the type of the file object

print("File is closed:", file_object.closed)  # Inform that the file is closed