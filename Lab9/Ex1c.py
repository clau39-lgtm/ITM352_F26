# Open a file and read its contents.

with open("names.txt", "r") as file_object:  # Open the file in read mode using 'with'
    contents = file_object.read()  # Read the contents of the file
    print(contents)  # Print the contents of the file
    contents_list = contents.splitlines()
    print(f"Number of names: {len(contents_list)}")  # Print the number of names in the file
    for name in contents_list:
        print(name)  # Print each name in the file