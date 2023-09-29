"""
Write a function, getX, that given an integer x and a list nums returns the Xth number if the list was in sorted order.
In other words, the Xth smallest number.
Function Name: getX
Input: An integer, x, and an unsorted list of integers nums that aren’t necessarily distinct
Output: The integer corresponding to the Xth number in the sorted list
"""


def getX(x, nums):
    if x > len(nums) or len(nums) == 0:
        return 0
    return sorted(nums)[x - 1]


print(getX(5, [5, 10, -3, -3, 7, 9]))
