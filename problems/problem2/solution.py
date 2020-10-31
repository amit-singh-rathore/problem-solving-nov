def merge_intervals(array):
    if len(array) < 2:
        return array

    result = [array[0]]
    for i in range(1, len(array)):
        if array[i][0] <= result[-1][1]:
            result[-1][1] = max(array[i][1], result[-1][1])
        else:
            result.append(array[i])
    return result

