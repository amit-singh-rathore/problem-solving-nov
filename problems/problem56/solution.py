def subarraySum(nums, k):
    count = 0
    cum_sum = 0
    l = len(nums)
    cum_sum_freq = {}
    cum_sum_freq[0] = 1

    for item in nums:
        cum_sum += item
        if (cum_sum - k) in cum_sum_freq:
            count += cum_sum_freq[cum_sum-k]
            
        if cum_sum in cum_sum_freq:
            cum_sum_freq[cum_sum] += 1
        else:
            cum_sum_freq[cum_sum] = 1
            
    return count
    
print(subarraySum([1,2,3], 3))