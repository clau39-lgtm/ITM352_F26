recent_purchases = [36.13, 23.87, 183.35, 22.93, 11.62]
budget = 60


def check_budget(purchases, budget):
    total_spent = 0
    results = []

    for purchase in purchases:
        total_spent += purchase
        if total_spent > budget:
            results.append(f"This purchase {purchase} exceeds the budget.")
            break
        results.append(f"This purchase {purchase} is within the budget.")

    return results
