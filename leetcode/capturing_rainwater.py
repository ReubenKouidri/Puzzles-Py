def capturing_rainwater(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    trapped_water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            trapped_water += max(0, left_max - height[left])
        else:
            right -= 1
            right_max = max(right_max, height[right])
            trapped_water += max(0, right_max - height[right])

    return trapped_water


def tests():
    assert capturing_rainwater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert capturing_rainwater([4, 2, 0, 3, 2, 5]) == 9
    assert capturing_rainwater([5, 4, 1, 2]) == 1
    assert capturing_rainwater(
        [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4,
         6, 8, 1, 3]) == 83
    assert capturing_rainwater([9, 6, 8, 8, 5, 6, 3]) == 3
    assert capturing_rainwater([8, 8, 1, 5, 6, 2, 5, 3, 3, 9]) == 31


if __name__ == "__main__":
    tests()
