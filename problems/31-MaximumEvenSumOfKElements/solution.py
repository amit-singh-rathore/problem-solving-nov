def get_max_even_sum (arr, k):
    if k > len(arr) or len(arr) == 0:
        return -1
        
    arr.sort(reverse = True)

    even_nums = [num for num in arr if num%2==0]
    odd_nums = [num for num in arr if num%2!=0]
    max_sum, even_idx, odd_idx = 0, 0, 0
    
    while k > 0:
        if k % 2 == 1:
            if (len(even_nums) > 0):
                max_sum += even_nums[even_idx]
                even_idx += 1
                k -= 1
            else:
                return -1
        else:
            if even_idx < len(even_nums) - 1 and odd_idx < len(odd_nums) - 1:
                max_sum += max(even_nums[even_idx] + even_nums[even_idx + 1], odd_nums[odd_idx] + odd_nums[odd_idx + 1])
                even_idx += 2
                odd_idx += 2
            elif even_idx < len(even_nums) - 1:
                max_sum += even_nums[even_idx] + even_nums[even_idx + 1]
                even_index += 2
            elif odd_idx < len(odd_nums) - 1:
                max_sum += odd_nums[odd_idx] + odd_nums[odd_idx + 1]
                odd_idx += 2
            
            k -= 2

    return max_sum  

print(get_max_even_sum([ 2, 4, 10, 3, 5 ], 3))