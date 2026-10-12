amount = 0.87
quarters = amount // 0.25
amount %= 0.25
dimes = amount // 0.10
amount %= 0.10
nickels = amount // 0.05
amount %= 0.05
pennies = amount
print(f"Quarters: {quarters}, Dimes: {dimes}, Nickels: {nickels}, Pennies: {pennies}")