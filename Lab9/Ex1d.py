# Read a file of names one line at a time and print each name.

with open("names.txt", "r") as file_object:  # Open the file in read mode using 'with'
    while (line := file_object.readline()):  # Read one line at a time
        print(line.strip())  # Print the line without leading/trailing whitespace