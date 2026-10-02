recent_purchases = [36.13, 23.87, 183.35, 22.93, 11.62]
budget = 60
totalSpent = 0

for purchase in recent_purchases:
    totalSpent += purchase
    if totalSpent > budget:
        print(f"This purchase {purchase} exceeds the budget.")
        break
    else:
        print(f"This purchase {purchase} is within the budget.")