data = ("hello", 10, "goodbye", 3, "goodnight", 5)
new_item = input("Enter a value to append: ")


try:
    data = list(data)
    data.append(new_item)
    data = tuple(data)
    print("Appended tuple:", data)
except Exception as e:
    print("Error:", e)