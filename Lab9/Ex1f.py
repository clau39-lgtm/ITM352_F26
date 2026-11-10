# Open names.txt and read its contents
# Append a new name at the end of the file.

with open("names.txt", "r") as file_object:  # Open the file in append mode using 'with'
    contents_list = file_object.readlines() 
    print(contents_list)  # Print the contents of the file as a list

with open ("names.txt", "a") as file_object:  # Open the file in append mode using 'with'
    print("Appending a new name to the file...")
    file_object.write("Doe, John\n")  # Append a new name at the end of the file