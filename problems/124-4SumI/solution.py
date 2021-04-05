class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        if n < 4:
            return []
        if nums[0]*4 > target or nums[-1]*4 < target:
            return []
        
        res = set()
        
        
        for i in range(n):
            for j in range(i+1, n):
                curr_sum = nums[i] + nums[j]
                remainder_sum = target - curr_sum
                x = j + 1
                y = n-1
                while (x < y):
                    s = nums[x] + nums[y]
                    if (s == remainder_sum):
                        res.add((nums[i], nums[j], nums[x], nums[y]))
                        x += 1
                        y -= 1
                    elif s < remainder_sum:
                        x += 1
                    else:
                        y -= 1

        return list(res)
