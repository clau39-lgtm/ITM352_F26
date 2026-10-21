import random

R1 = random.randint(1, 10)
R2 = random.randint(1, 10)

if R2 == R1:
    R2 = random.randint(1, 10)

print("Random number 1:", R1)
print("Random number 2:", R2)