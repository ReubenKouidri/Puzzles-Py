"""
The Knapsack Problem
Imagine that you are a thief breaking into a house.
There are so many valuables to steal, 
but you’re just one person who can only carry so much. 
Each item has a weight and value, 
and your goal is to maximize the total value of items
while remaining within the weight limit of your knapsack.

Create a knapsack() function that takes in:
    the total amount of weight you can carry,
    an array of the weights of all of the items,
    an array of the values of all of the items,
    and returns the maximum value that you will be able to carry.

For example, let’s say your knapsack can carry 10 units of weight.
The item weights are [3, 6, 8] and their values are [50, 60, 100].
Your knapsack function should return 110 since you can carry the first and second items,
whose values total 110.
If you tried to carry the third item, which has the value of 100,
you wouldn’t be able to fit anything else in the knapsack.
"""


def knapsack(weight_cap: int, weights: list[int], values: list[int]) -> int:
    possible_combos = []

    if not weights or not values or len(weights) == 0 or len(values) == 0 or weight_cap == 0:
        return 0

    for i in range(len(weights)):
        if weights[i] > weight_cap:
            continue
        combo = [values[i]]
        combo_weight = weights[i]
        for j in range(i, len(weights)):
            if j == i:
                continue
            if combo_weight + weights[j] <= weight_cap:
                combo.append(values[j])
                combo_weight += weights[j]
        possible_combos.append(combo)

    return max(sum(combo) for combo in possible_combos)


weight_cap = 5
weights = [1, 1, 3, 5]
values = [250, 200, 300, 500]
print(knapsack(weight_cap, weights, values))
