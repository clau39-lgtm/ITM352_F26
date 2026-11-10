# Open a file of names and print its type.

file_object = open("test.txt", "r")  # Open the file in read mode
print(type(file_object))  # Print the type of the file object
file_object.close()  # Close the file