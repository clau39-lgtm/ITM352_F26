emotions = ("happy", "sad", "fear", "surprised", "anxious")

is_it_true = emotions[len(emotions)-1] == "happy" and len(emotions) > 3
print(is_it_true)

if emotions[len(emotions) - 1] == "happy" and len(emotions) > 3:
    is_it_true = True
else:
    is_it_true = False

print(is_it_true)