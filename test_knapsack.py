from unittest import TestCase

from knapsack import knapsack


class Test(TestCase):
    def test_empty_weights_and_vals(self):
        self.assertEqual(knapsack(10, [], []), 0)

    def test_single_elements(self):
        self.assertEqual(knapsack(10, [5], [3]), 3)

    def test_multiple_elements(self):
        self.assertEqual(knapsack(10, [1, 2, 3, 4], [6, 10, 12, 8]), 36)

    def test_weights_gt_weight_cap(self):
        self.assertEqual(knapsack(10, [5, 6, 7, 8], [3, 4, 5, 6]), 6)

    def test_weights_equal_weight_cap(self):
        self.assertEqual(knapsack(10, [5, 5, 5], [3, 4, 5]), 9)

    def test_weights_lt_weight_cap(self):
        self.assertEqual(knapsack(10, [1, 2, 3], [6, 10, 12]), 28)

    def test_none_weights_none_vals(self):
        self.assertEqual(knapsack(10, None, None), 0)

    # Test case 9: Weights and values with weights and values as None and empty lists
    def test_none_weights_empty_vals(self):
        self.assertEqual(knapsack(10, None, []), 0)

    # Test case 10: Weights and values with weights and values as empty lists and None
    def test_empty_weights_none_vals(self):
        self.assertEqual(knapsack(10, [], None), 0)
