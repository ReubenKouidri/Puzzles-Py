def flatten_array(arr):
    result = []
    for element in arr:
        if not isinstance(element, int):
            result.extend(flatten_array(element))
        else:
            result.append(element)
    return result


array = [1, 2, [[3, 4, 5], [6, 7]], 8, [9, 10], 11]

print(flatten_array(array))