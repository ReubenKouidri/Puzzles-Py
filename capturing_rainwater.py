def find_highest_rhs(array, lhs_index):
    highest_rhs = 0
    for i in range(lhs_index + 1, len(array)):
        highest_rhs = max(highest_rhs, array[i])
    return highest_rhs, array[lhs_index:].index(highest_rhs) + lhs_index


def capturing_rainwater(heights):
    volumes = [0] * len(heights)
    lhs_index = 0
    while heights[lhs_index] <= heights[lhs_index + 1]:
        lhs_index += 1

    highest_lhs = heights[lhs_index]
    rhs_idx = lhs_index

    while rhs_idx + 1 < len(heights):
        highest_rhs, rhs_idx = find_highest_rhs(heights, lhs_index)
        max_fill = min(highest_rhs, highest_lhs)

        for i in range(lhs_index + 1, rhs_idx):  # fill between the lhs and rhs indices
            volumes[i] = max_fill - heights[i]

        lhs_index = rhs_idx
        highest_lhs = highest_rhs

    return sum(volumes)


test_array = [4, 2, 1, 3, 0, 1, 2]
test_array2 = [1, 2, 1, 3, 0, 1, 2]
test_array3 = [0, 1, 2, 3, 0, 1, 2]
# print(capturing_rainwater(test_array))
# print(capturing_rainwater(test_array2))
print(capturing_rainwater(test_array3))
