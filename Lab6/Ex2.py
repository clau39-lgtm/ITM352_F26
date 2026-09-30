# Create a list with a variety of values
my_list = [10, "apple", True, 3.5, "watermelon", "carrot", 99, None, "horse"]

if len(my_list) < 5:
    print("The list has fewer than 5 elements.")
elif 5 <= len(my_list) <= 10:
    print("The list has between 5 and 10 elements.")
else:
    print("The list has more than 10 elements.")

# Test with several different list lengths
test_lists = [
    [1, 2],
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50, 60],
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
]

for items in test_lists:
    if len(items) < 5:
        print(f"{items} -> fewer than 5 elements")
    elif 5 <= len(items) <= 10:
        print(f"{items} -> between 5 and 10 elements")
    else:
        print(f"{items} -> more than 10 elements")