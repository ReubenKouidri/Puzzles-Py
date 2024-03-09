"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is greater than or equal to
 target. If there is no such subarray, return 0 instead.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem
constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
"""

import math


def min_subarray_len(target, nums):
    """ contiguous, non-empty sequence of elements within an array """
    l, s = 0, 0
    min_len = math.inf

    for i, num in enumerate(nums):
        s += num
        while s >= target:
            min_len = min(min_len, i - l + 1)
            s -= nums[l]
            l += 1

    return min_len if min_len != math.inf else 0


def test():
    assert min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2
    assert min_subarray_len(4, [1, 4, 4]) == 1
    assert min_subarray_len(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert min_subarray_len(15, [1, 2, 3, 4, 5]) == 5
    assert min_subarray_len(213,
                            [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]) == 8


if __name__ == "__main__":
    test()
