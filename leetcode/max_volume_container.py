def find_max_volume(height):
    max_vol = 0
    l, r = 0, len(height) - 1
    while l < r:
        left_height = height[l]
        right_height = height[r]
        max_vol = max(max_vol, min(left_height, right_height) * (r - l))
        if left_height <= right_height:
            l += 1
        else:
            r -= 1
    return max_vol


def test():
    assert find_max_volume([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert find_max_volume([1, 1]) == 1
    assert find_max_volume([1, 2, 4, 3]) == 4
    print("PASSED!")


if __name__ == "__main__":
    test()
