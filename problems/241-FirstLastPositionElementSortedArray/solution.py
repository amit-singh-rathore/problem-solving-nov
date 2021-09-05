class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        def find_boundary(nums, targ, lower_or_upper):
            start, mid, end = 0, 0, len(nums)-1

            while start <= end:
                mid = start + (end-start)//2
                if nums[mid] == target:
                    if lower_or_upper == 'lower':
                        if mid == start or nums[mid-1] < target:
                            return mid
                        end = mid - 1
                    elif lower_or_upper == 'upper':
                        if mid == end or nums[mid+1] > target:
                            return mid                        
                        start = mid + 1                        
                elif nums[mid] > target:
                    end = mid -1
                else:
                    start = mid + 1
            
            return -1
                


        first_idx = find_boundary(nums, target, 'lower')

        last_idx = find_boundary(nums, target, 'upper')

        return [first_idx, last_idx]

        