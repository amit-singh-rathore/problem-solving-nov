def pair_count(nums, d, n):
    i, j, cnt = 0, 0, 0
    for i in range(n):
        while nums[i] - nums[j] > d and j < i:
            j += 1
            cnt += (n - i)
    res = ((n * (n - 1)) >> 1) - cnt
    return res

def smallest_distance_pairs(nums, k):
    nums.sort()
    n = len(nums)
    min_distance = min(nums[idx + 1] - nums[idx] for idx in range(n - 1))
    max_distance = nums[-1] - nums[0]
    while min_distance <= max_distance:
        mid = min_distance + ((max_distance - min_distance) >> 1)
        if k <= pair_count(nums, mid, n):
            max_distance = mid - 1
        else:
            min_distance = mid + 1
    return min_distance
print(smallest_distance_pairs([1,4, 6, 0, 1, 10], 8))

