evens = [2]
nums = 2

while evens[-1] < 50:
    nums += 2
    evens.append(nums)

print(evens)