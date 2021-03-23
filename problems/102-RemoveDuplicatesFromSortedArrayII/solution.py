class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx_to_update, num_rep = 1, 1

        for idx, num in enumerate(nums[1:]):
            num_rep = num_rep+1 if num == nums[idx] else 1
            if num_rep <= 2:
                nums[idx_to_update] = num
                idx_to_update += 1
        return idx_to_update