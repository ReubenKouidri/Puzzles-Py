"""
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
"""


def two_sum_slow(nums, tgt):
    for l in range(len(nums) - 1):
        for r in range(l + 1, len(nums)):
            if nums[l] + nums[r] == tgt:
                return [l, r]


def two_sum_fast(nums, tgt):
    hash_table = {}
    for i, num in enumerate(nums):
        compliment = tgt - num
        if compliment in hash_table:
            return [hash_table[compliment], i]
        hash_table[num] = i


def test():
    assert two_sum_slow([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum_fast([2, 7, 11, 15], 9) == [0, 1]

    assert two_sum_slow([3, 2, 4], 6) == [1, 2]
    assert two_sum_fast([3, 2, 4], 6) == [1, 2]

    assert two_sum_slow([3, 3], 6) == [0, 1]
    assert two_sum_fast([3, 3], 6) == [0, 1]
    print("PASSED!")


if __name__ == "__main__":
    test()
