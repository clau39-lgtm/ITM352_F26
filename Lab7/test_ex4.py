import unittest

from Ex4 import check_budget


class TestCheckBudget(unittest.TestCase):
    def test_all_purchases_within_budget(self):
        purchases = [10, 20, 15]
        budget = 60
        expected = [
            "This purchase 10 is within the budget.",
            "This purchase 20 is within the budget.",
            "This purchase 15 is within the budget.",
        ]
        self.assertEqual(check_budget(purchases, budget), expected)

    def test_purchase_exceeds_budget(self):
        purchases = [36.13, 23.87, 183.35, 22.93]
        budget = 60
        expected = [
            "This purchase 36.13 is within the budget.",
            "This purchase 23.87 is within the budget.",
            "This purchase 183.35 exceeds the budget.",
        ]
        self.assertEqual(check_budget(purchases, budget), expected)

    def test_exact_budget_is_allowed(self):
        purchases = [30, 30]
        budget = 60
        expected = [
            "This purchase 30 is within the budget.",
            "This purchase 30 is within the budget.",
        ]
        self.assertEqual(check_budget(purchases, budget), expected)

    def test_empty_purchase_list(self):
        self.assertEqual(check_budget([], 50), [])


if __name__ == "__main__":
    unittest.main()
