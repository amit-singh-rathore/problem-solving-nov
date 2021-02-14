def jump(nums):
    curr_end = 0
    max_finish = 0
    jumps = 0

    for i in range(len(nums)-1):
        max_finish = max(max_finish, i+nums[i]);
        if curr_end ==i:
            jumps += 1
            curr_end = max_finish
    return jumps
        

print(jump([2,3,1,1,4]))