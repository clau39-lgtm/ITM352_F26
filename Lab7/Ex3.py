data = ("hello", 10, "goodbye", 3, "goodnight", 5)

stringCount = 0
for item in data:
    if type(item) == str:
        stringCount += 1

print(f"There are {stringCount} strings in the tuple.")