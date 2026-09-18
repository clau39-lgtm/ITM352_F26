# Properly format an inputted name in title case

raw_name = input("Enter a name: ")

stripped_name = raw_name.strip()    
title_name = stripped_name.title()
print("Formatted name in title case:",title_name)